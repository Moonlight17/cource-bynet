data "aws_availability_zones" "available" {}

locals {
  cluster_name = "bynet-bootcamp-${random_string.suffix.result}"
}

resource "random_string" "suffix" {
  length  = 8
  special = false
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "3.14.0"

  name                  = "bynet-vpc"
  cidr                  = "192.168.0.0/16"
  azs                   = data.aws_availability_zones.available.names
  database_subnets       = ["192.168.96.0/24", "192.168.128.0/24",]
  public_subnets        = ["192.168.0.0/24", "192.168.32.0/24",]
  enable_nat_gateway    = true
  single_nat_gateway    = true
  enable_dns_hostnames  = true

  tags = {
    "kubernetes.io/cluster/${local.cluster_name}" = "shared"
  }

  public_subnet_tags = {
    "kubernetes.io/cluster/${local.cluster_name}" = "shared"
    "kubernetes.io/role/elb"                      = "1"
  }

  database_subnet_tags = {
    "kubernetes.io/cluster/${local.cluster_name}" = "shared"
    "kubernetes.io/role/internal-elb"             = "1"
  }
}