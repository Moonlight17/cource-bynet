terraform {
  backend "s3" {
    bucket = "bynet-bucket"
    key    = "tf-states/rds-state.tfstate"
    region = "eu-west-2"
    profile = "dev-backup"
  }
}

provider "aws" {
  region = var.region
  profile = var.profile
}

data "terraform_remote_state" "vpc" {
  backend = "s3"
  config = {
    bucket  = "bynet-bucket"
    key     = "tf-states/vpc-state.tfstate"
    region  = "eu-west-2"
    profile = "dev-backup"
  }
}
