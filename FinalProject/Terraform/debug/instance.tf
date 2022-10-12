# Provide RDS instance
# resource "aws_db_subnet_group" "bynet" {
#   name       = "main"
#   subnet_ids = data.terraform_remote_state.vpc.outputs.database_subnets

#   tags = {
#     Name = "My DB subnet group"
#   }
# }

resource "aws_instance" "work_service" {
  ami                    = "ami-0e34bbddc66def5ac" //Amazon Linux
  instance_type          = "t3.micro"
  vpc_security_group_ids = [aws_security_group.group_for_work_service.id]
  user_data              = file("user_data.sh")
  user_data_replace_on_change = true # Added in the new AWS provider!!!

  tags = {
    Name  = "Working instance",
    Owner = "DevOps"
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
