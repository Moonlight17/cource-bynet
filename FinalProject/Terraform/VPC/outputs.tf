
output "cluster_name" {
  description = "Kubernetes Cluster Name"
  value       = local.cluster_name
}

output "database_subnets" {
  description = "EKS private subnets"
  value       = module.vpc.database_subnets
}

output "public_subnets" {
  description = "EKS private subnets"
  value       = module.vpc.public_subnets
}

output "nodes_sg" {
  description = "Security group for nodes"
  value       = aws_security_group.all_worker_mgmt.id
}

output "vpc_id" {
  description = "Security group for nodes"
  value       = module.vpc.vpc_id

}

