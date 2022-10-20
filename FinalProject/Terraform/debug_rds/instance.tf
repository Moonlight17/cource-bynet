# Provide RDS instance
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
  vpc_security_group_ids = [aws_security_group.group_for_work_service.id]




  # db_subnet_group_name   = aws_db_subnet_group.default.name
  # vpc_security_group_ids = [aws_security_group.all_worker_mgmt.id]

  tags = {
    Name = "bynet-rds"
  }
}

resource "aws_security_group" "group_for_work_service" {
  name        = "work_service-SG"
  description = "Security grup for ny work_service"
  ingress {
    description = "Port for HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    description = "Port for HTTPS"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    description = "ALLOW ALL Port"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name  = "SG instance",
    Owner = "DevOps"
  }
}
