# Create a file we can run locally to configure OIDC

# Steps
# Create Azure AD application / service principle
# Add federated credentials
# GitHub secrets?
# Setup Login
# Probably going to use CLI

terraform {
  required_providers {
    github = {
      source = "integrations/github"
    }
  }
}

provider "github" {
  # Replace with your GitHub access token
  token = ""
}

provider "azuread" {
  version = "~> 2.0"
}

resource "azuread_application" "example" {
  name                   = "example-app"
  homepage               = "https://example.com"
  identifier_uris        = ["https://example.com"]
  reply_urls             = ["https://example.com/callback"]
  available_to_other_tenants = false

  oauth2_allow_implicit_flow = true

  oauth2_permissions {
    admin_consent_description  = "Allow access to the example app"
    admin_consent_display_name = "Example App Access"
    is_enabled                 = true
    type                       = "User"
    value                      = "User.Read"
  }
}

resource "azuread_application_password" "example" {
  application_object_id = azuread_application.example.object_id
  value                 = "MySecretPassword123!"
  end_date_relative     = "720h"  # Set a long expiration for the password
}

resource "azuread_service_principal" "example" {
  application_id               = azuread_application.example.application_id
  app_role_assignment_required = false
}

resource "azuread_service_principal_password" "example" {
  service_principal_id = azuread_service_principal.example.id
  value                = "MySecretPassword456!"
  end_date_relative    = "720h"  # Set a long expiration for the password
}

resource "github_actions_organization_secrets" "example" {
  secret_name = "AZURE_CLIENT_ID"
  plaintext_value = azuread_application.example.application_id
  repository_selection = "all"
}

resource "github_actions_organization_secrets" "example" {
  secret_name = "AZURE_TENANT_ID"
  plaintext_value = data.azurerm_client_config.current.tenant_id
  repository_selection = "all"
}

resource "github_actions_organization_secrets" "example" {
  secret_name = "AZURE_CLIENT_SECRET"
  plaintext_value = azuread_application_password.example.value
  repository_selection = "all"
}

data "azurerm_client_config" "current" {}

output "client_id" {
  value = azuread_application.example.application_id
}

output "client_secret" {
  value = azuread_application_password.example.value
}

output "tenant_id" {
  value = data.azurerm_client_config.current.tenant_id
}
