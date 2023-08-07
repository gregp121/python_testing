# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MPL-2.0

variable "tfc_aws_audience" {
  type        = string
  # default     = "aws.workload.identity"
  default = "sts.amazonaws.com" # This will allow the AWS Security Token Service to be called
  description = "The audience value to use in run identity tokens"
}

variable "tfc_hostname" {
  type        = string
  default     = "app.terraform.io"
  description = "The hostname of the TFC or TFE instance you'd like to use with AWS"
}

# variable "tfc_organization_name" {
#   type        = string
#   description = "The name of your Terraform Cloud organization"
# }

variable "tfc_project_name" {
  type        = string
  default     = "python_testing"
  description = "The project under which a workspace will be created"
}

variable "tfc_workspace_name" {
  type        = string
  default     = "my-aws-workspace"
  description = "The name of the workspace that you'd like to create and connect to AWS"
}

variable "repo_name" {
  type        = string
  default     = "python_testing"
  description = "The name of the repository that you'd like to create and connect to AWS"
}

variable "branch" {
  type        = string
  default     = "main"
  description = "The name of the repository branch that you'd like to create and connect to AWS"
}

