variable "region" {
  default     = "eu-west-2"
  description = "AWS region"
}
variable "profile" {
  default     = "dev-backup"
  description = "AWS Profile"
}


variable "db_name" {
  default     = "postgres"
}
variable "db_username" {
  default     = "postgres"
}
variable "db_password" {
  default     = "1q2w3e4r"
}
