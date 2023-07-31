provider "aws" {
}

# Data source used to grab the TLS certificate for Terraform Cloud.
#
# https://registry.terraform.io/providers/hashicorp/tls/latest/docs/data-sources/certificate
# data "tls_certificate" "tfc_certificate" {
#   url = "https://${var.tfc_hostname}"
# }

# Creates an OIDC provider which is restricted to
#
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_openid_connect_provider

# AWS secures comms with Github using trusted CAs - NOTE: This only connects to github
## Old value: url             = data.tls_certificate.tfc_certificate.url
## We should probably use the URL we got the thumbprint from
resource "aws_iam_openid_connect_provider" "github_provider" {
  url             = "https://token.actions.githubusercontent.com"
  client_id_list  = [var.tfc_aws_audience]
  thumbprint_list = ["1c58a3a8518e8759bf075b76b750d4f2df264fcd"]
}

## AFTER CREATING PROVIDER, WE NEED THE ROLE ATTACHED TO IT


# Creates a role which can only be used by the specified Terraform
# cloud workspace.
#
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role

### NOTEL Federated role can be found when editing the trust relationship of a created role

## NOTE: Originally approved main, not Terraform branch - ${var.branch}
resource "aws_iam_role" "github_role" {
  name = "github-role"

  assume_role_policy = <<EOF
{
 "Version": "2012-10-17",
 "Statement": [
   {
     "Effect": "Allow",
     "Principal": {
       "Federated": "arn:aws:iam::889496399080:oidc-provider/token.actions.githubusercontent.com"
     },
     "Action": "sts:AssumeRoleWithWebIdentity",
     "Condition": {
       "StringEquals": {
         "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
       },
       "StringLike": {
         "token.actions.githubusercontent.com:sub": "repo:gregp121/${var.repo_name}:*"
       }
     }
   }
 ]
}
EOF
}

# Creates a policy that will be used to define the permissions that
# the previously created role has within AWS.
#
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_policy
resource "aws_iam_policy" "git_policy" {
  name        = "git-policy"
  description = "GIT run policy"

  policy = <<EOF
{
 "Version": "2012-10-17",
 "Statement": [
   {
     "Effect": "Allow",
     "Action": [
       "s3:ListBucket"
     ],
     "Resource": "*"
   }
 ]
}
EOF
}

# Creates an attachment to associate the above policy with the
# previously created role.
#
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy_attachment
resource "aws_iam_role_policy_attachment" "git_policy_attachment" {
  role       = aws_iam_role.github_role.name
  policy_arn = aws_iam_policy.git_policy.arn
}
