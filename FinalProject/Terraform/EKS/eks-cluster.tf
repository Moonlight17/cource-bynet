module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  version         = "18.20.5"
  cluster_name    = data.terraform_remote_state.vpc.outputs.cluster_name
  cluster_version = "1.21"
  subnet_ids      = data.terraform_remote_state.vpc.outputs.public_subnets
  # subnet_ids      = module.vpc.public_subnets
  vpc_id          = data.terraform_remote_state.vpc.outputs.vpc_id
  
  cluster_endpoint_private_access = true
  cluster_endpoint_public_access  = true
  cluster_enabled_log_types       = []
  create_cloudwatch_log_group     = false
  
# EKS Managed Node Group(s)
  eks_managed_node_group_defaults = {
    # disk_size      = 50
    instance_types = ["t3.micro"]
  }


#   eks_managed_node_groups = {
#     # blue = {}
#     green = {
#       min_size     = 1
#       max_size     = 10
#       desired_size = 1

#       instance_types = ["t3.micro"]
#       capacity_type  = "SPOT"
#     }
#     # vpc_security_group_ids = [
#     #   data.terraform_remote_state.vpc.output.nodes_sg.id
#     # ]
#   }
  tags = {
    Stage = "Now"
  }


eks_managed_node_groups = {
    one = {
      name = "node-group-1"

      instance_types = ["t3.micro"]
      capacity_type  = "SPOT"

      desired_size = 2
      min_size     = 1
      max_size     = 5

      # pre_bootstrap_user_data = <<-EOT
      # echo 'foo bar'
      # EOT

      vpc_security_group_ids = [
        data.terraform_remote_state.vpc.outputs.nodes_sg
      ]
      labels = {
        environment = "staging"
      }
    }

    two = {
      name = "node-group-2"

      # instance_types = ["t3.micro"]
      instance_types = ["t3.medium"]
      capacity_type  = "SPOT"
      disk_size      = 20

      desired_size = 1
      min_size     = 1
      max_size     = 1

      # pre_bootstrap_user_data = <<-EOT
      # echo 'foo bar'
      # EOT

      vpc_security_group_ids = [
        data.terraform_remote_state.vpc.outputs.nodes_sg
      ]
      labels = {
        environment = "prod"
      }
    }
  }
}
