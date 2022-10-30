# provider "helm" {
#   kubernetes {
#     host                   = data.aws_eks_cluster.cluster.endpoint
#     cluster_ca_certificate = base64decode(data.aws_eks_cluster.cluster.certificate_authority.0.data)
#     exec {
#       api_version = "client.authentication.k8s.io/v1beta1"
#       args        = ["eks", "get-token", "--cluster-name", data.aws_eks_cluster.cluster.name]
#       command     = "aws"
#     }
#   }
# }


provider "helm" {
  kubernetes {
    config_path = "/Users/moonlight/Documents/Work/Bynet/FinalProject/Kubernetes/eksconfig"
  }
}
# provider "helm" {
#   kubernetes {
#     host                   = data.aws_eks_cluster.cluster.endpoint
#     cluster_ca_certificate = base64decode(data.aws_eks_cluster.cluster.certificate_authority.0.data)
#     exec {
#       api_version = "client.authentication.k8s.io/v1beta1"
#       args        = ["eks", "get-token", "--profile dev-backup", "--cluster-name", data.aws_eks_cluster.cluster.name]
#       command     = "aws"
#     }
#   }
# }
# /Users/moonlight/Documents/Work/Bynet/FinalProject/Kubernetes/eksconfig

# aws eks get-token --cluster-name https://AF30E1FF4AC0183CE488DF847450A72C.gr7.eu-west-2.eks.amazonaws.com/version --profile dev-backup





# Later may will Jenkins slave/node/agent
# resource "helm_release" "gitlab-agent" {
#   name             = "gitlab-agent"
#   repository       = "https://charts.gitlab.io"
#   chart            = "gitlab-agent"
#   namespace        = "gitlab-agent"
#   create_namespace = true

#   set {
#     name  = "config.token"
#     value = var.gitlab_agent_token
#   }
#   set {
#     name  = "config.kasAddress"
#     value = "wss://kas.gitlab.com"
#   }  
# }

resource "helm_release" "metrics-server" {
  name             = "metrics-server"
  repository       = "https://kubernetes-sigs.github.io/metrics-server/"
  chart            = "metrics-server"
  namespace        = "kube-system"

  values = [
    "${file("values/metrics-server.yaml")}"
  ]
}

resource "helm_release" "fluent-bit" {
  name             = "fluent-bit"
  repository       = "https://aws.github.io/eks-charts"
  chart            = "aws-for-fluent-bit"
  namespace        = "kube-system"

  values = [
    "${file("values/fluent-bit.yaml")}"
  ]
}

resource "helm_release" "kubernetes-dashboard" {
  name             = "kubernetes-dashboard"
  repository       = "https://kubernetes.github.io/dashboard/"
  chart            = "kubernetes-dashboard"

  values = [
    "${file("values/kubernetes-dashboard.yaml")}"
  ]
}

resource "helm_release" "aws-cloudwatch-metrics" {
  name             = "aws-cloudwatch-metrics"
  repository       = "https://aws.github.io/eks-charts"
  chart            = "aws-cloudwatch-metrics"
  namespace        = "cloudwatch-metrics"
  create_namespace = true

  set {
    name  = "clusterName"
    value = data.terraform_remote_state.eks.outputs.cluster_id
  }
}
