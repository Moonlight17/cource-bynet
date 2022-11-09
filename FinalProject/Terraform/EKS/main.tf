provider "kubernetes" {
  host                   = module.eks.cluster_endpoint
  cluster_ca_certificate = base64decode(module.eks.cluster_certificate_authority_data)
}

terraform {
  backend "s3" {
    bucket = "bynet-bucket"
    key    = "tf-states/eks-state.tfstate"
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


data "aws_availability_zones" "available" {}

locals {
  cluster_name = data.terraform_remote_state.vpc.outputs.cluster_name
}

resource "random_string" "suffix" {
  length  = 8
  special = false
}

data "aws_eks_cluster_auth" "cluster" {
  name = module.eks.cluster_id
}

provider "helm" {
  kubernetes {
    host                   = module.eks.cluster_endpoint
    cluster_ca_certificate = base64decode(module.eks.cluster_certificate_authority_data)
    token                  = data.aws_eks_cluster_auth.cluster.token
  }
}

