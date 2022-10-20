# Provide RDS instance
resource "aws_db_subnet_group" "bynet" {
  name       = "main"
  subnet_ids = data.terraform_remote_state.vpc.outputs.database_subnets

  tags = {
    Name = "My DB subnet group"
  }
}


resource "aws_db_instance" "rds" {
  identifier             = "bynet-rds"
  allocated_storage      = 5
#   storage_type           = "gp2"
  engine                 = "postgres"
  engine_version         = "14"
  instance_class         = "db.t3.micro"
  db_name                = var.db_name
  username               = var.db_username
  password               = var.db_password
  parameter_group_name   = "default.postgres14"
  skip_final_snapshot    = true
  # publicly_accessible    = true # for local debug
  multi_az               = false

  db_subnet_group_name   = aws_db_subnet_group.bynet.name
  vpc_security_group_ids = [data.terraform_remote_state.vpc.outputs.nodes_sg]




  # db_subnet_group_name   = aws_db_subnet_group.default.name
  # vpc_security_group_ids = [aws_security_group.all_worker_mgmt.id]

  tags = {
    Name = "bynet-rds"
  }
}
