---
marp: true
theme: your-theme
_class: lead
paginate: true    
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
size: 16:9
---
# Slide 0: Introduction
Ebrahim Ramadan
Cloud Architect at Accenture Baltics
##Certifications:
CKA (Certified Kubernetes Administrator)
CKAD (Certified Kubernetes Application Developer)
KCNA (Kubernetes Certified Network Administrator)
SAA (AWS Solution Architect Associate)

Core Skills:
 AWS
 Kubernetes
 Docker
 Istio.io
 GitOps
 CI/CD
 Crossplane

Experience:
 13 years of experience in the computer software industry
 Worked with 5 companies
 22 projects
 
---
# Slide 1: Introduction
- Brief overview of the problem of managing infrastructure resources across multiple cloud providers
- Introduction to Crossplane as a solution for multi-cloud management

---
# Slide 2: Key Features of Crossplane
-	Composite resources and claims:
-	Provider abstraction:
-	Multi-cloud management:
-	Infrastructure as code:
-	Cost management:

---
# Slide 3: How Crossplane Works
-	Overview of the installation and configuration process
-	Explanation of the components of Crossplane (e.g. Provider, Composite resource, Claim)
-	Diagrams or visual aids to help explain the process

---
# Slide 4: Use Cases of Crossplane
-	Multi-cloud management:
-	Infrastructure as code:
-	Cost management:
-	Improved security:
-	Improved collaboration:
-	Container networking and security
-	Database as a service:
---
# Slide 5: Benefits of Using Crossplane
-	Reduced vendor lock-in:
-	Improved efficiency:
-	Better cost management:
-	Improved security:
-	Improved governance: 
-	Improved collaboration:

---
# Slide 6: Real-world Examples
-	Use cases of Crossplane in production
-	Examples of companies that are using Crossplane
** Adobe
** Ticketmaster
**	GoDaddy
**	Shopify
**	OpenAI
**	Twitch

---
# Slide 7: How to Get Started with Crossplane
- Getting started with Crossplane is relatively simple and can be broken down into the following steps:
- Links to documentation and resources:

---
# Slide 8: Best Practices for Using Crossplane
- Using Crossplane effectively requires following certain best practices:

---
# Slide 9: Crossplane vs (terraform and CDK for Terraform ) vs Pulumi

- Terraform vs. Pulumi vs. Crossplane – Infrastructure as Code (IaC) Tools Compared

---
# My story:

The story about a company that is moving their infrastructure and applications from a private cloud to a public cloud, specifically using AWS. They have a mix of different types of applications, including Kubernetes, Cloud Foundry, and VMs. The customer wants to use a unified approach and adopt cloud native technologies and practices in the process. The team has gone through various tools and solutions in their migration journey, including terraform, cloudfromthon, CDK, and now crossplane and argocd. The current system uses AWS Service Catalog and CloudFormation and CDK, but they are now looking to implement crossplane and argocd as a solution.

I have moved from team to team and have encountered teams that use different infrastructure as code (IAC) tools. This has highlighted the benefits of using crossplane and argocd as a solution, as it provides a unified approach and allows for more consistent and efficient management of the infrastructure and applications in the migration process. Additionally, Crossplane allows for multi-cloud deployment and can abstract the complexities of different public cloud providers, and argocd is a declarative GitOps solution that enables continuous delivery and Git-based collaboration, making it a great fit for the migration process.

---
# Summary
What is Crossplane?
Crossplane is an open-source multi-cloud control plane that enables users to provision and manage infrastructure resources across multiple cloud providers. It allows users to define infrastructure resources as code, such as a PostgreSQL database instance, and use a single API to provision and manage those resources across different cloud providers. Crossplane uses a concept of composite resources and claims to provide a consistent and unified way to provision and manage infrastructure resources, similar to how Persistent Volumes (PVs) and Persistent Volume Claims (PVCs) work in Kubernetes.

Why use Crossplane?
Users may choose to use Crossplane to reduce vendor lock-in, improve efficiency, better manage costs, improve security, improve governance, and improved collaboration. By abstracting away the underlying infrastructure, Crossplane makes it easier to move workloads between different cloud providers, streamline operations, and manage resources and costs more effectively. With Crossplane, you can create policies and governance rules that can be applied to your infrastructure, which can help to ensure that resources are provisioned and managed in compliance with your organization's policies.

How to use Crossplane?
To use Crossplane, you first need to install a working Kubernetes cluster. Then, you can install the Crossplane CLI, which is a command-line tool that can be used to install and manage Crossplane components in the cluster. Next, you can install Crossplane and configure a provider by creating a Provider resource that includes the provider's credentials. Additional providers can be installed if needed, then you can create composite resources, claims, and configure the composition. Finally, you can install a configuration package that defines the resources you want to provision and manage.

Crossplane Alternatives 
Terraform, and Pulumi are all Infrastructure as Code (IAC) tools that allow users to manage their infrastructure using code. Each tool has its own unique features and strengths, as well as different requirements and supported resources. The choice between the three tools will depend on the specific use case and requirements of the organization or individual. Additionally, Crossplane uses Kubernetes manifests for resource definition, Terraform uses HashiCorp Configuration Language (HCL) and Pulumi allows users to write code in various programming languages such as JavaScript, Python, Go, and C#. All three tools support GitOps workflows and integrate well with CI/CD pipelines.
