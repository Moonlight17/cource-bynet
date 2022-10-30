terraform {
  backend "s3" {
    bucket = "bynet-bucket"
    key    = "tf-states/helm-state.tfstate"
    region  = "eu-west-2"
    profile = "dev-backup"
  }
}
provider "aws" {
  region = var.region
  profile = var.profile
}

data "terraform_remote_state" "eks" {
  backend = "s3"
  config = {
    bucket = "bynet-bucket"
    key = "tf-states/eks-state.tfstate"
    region  = "eu-west-2"
    profile = "dev-backup"
  }
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

locals {
  cluster_name = data.terraform_remote_state.vpc.outputs.cluster_name
}
