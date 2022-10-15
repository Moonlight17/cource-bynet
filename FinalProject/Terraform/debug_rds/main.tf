
terraform {
  backend "s3" {
    bucket  = "bynet-bucket"
    key     = "tf-states/debug-state.tfstate"
    region  = "eu-west-2"
    profile = "dev-backup"
  }
}
provider "aws" {
  region = var.region
  profile = var.profile
}

locals {
  cluster_name = "DEBUG---${random_string.suffix.result}"
}

resource "random_string" "suffix" {
  length  = 8
  special = false
}
