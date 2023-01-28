---
marp: true
theme: gaia
_class: lead
paginate: true 
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
size: 16:9

---

# Introduction
- Ebrahim Ramadan Cloud Architect at Accenture Baltics

- Certifications: CKA CKAD KCNA SAA

- Core Skills: AWS Kubernetes Docker Istio.io GitOps CI/CD Crossplane

- Experience: 13 years of experience in the computer software industry Worked with 5 companies 22 projects

---

# What Is Kubernetes? 
* Kubernetes is an open-source container orchestration system for automating the deployment, scaling, and management of containerized applications.

* It was originally developed by Google and is now maintained by the Cloud Native Computing Foundation (CNCF).

* Kubernetes provides a platform-agnostic way to manage and deploy containerized applications, making it possible to run them on a variety of infrastructure, including on-premises, in the cloud, or in a hybrid environment.

![bg left:10% 80%](https://kubernetes.io/images/favicon.png)

---

# Why use Kubernetes?

- Scalability

- High availability 

- Self-healing 

- Load balancing

- Flexibility 

- Automated rollouts and rollbacks

- Reduced operational overhead 

- Large and active community

![bg left:10% 80%](https://kubernetes.io/images/favicon.png)

----
# How Kubernetes works?
Kubernetes works by using a master-slave architecture to manage containerized applications:

- The developer uses kubectl command line tool to interact with the Kubernetes master node, which controls worker nodes.
- The worker nodes run the containerized application and communicate with the master node to ensure desired state is met.
- Kubernetes automatically distributes incoming traffic, monitor the running containers, and performs self-healing if needed.
- The developer can scale and update the application through the Kubernetes API server.

---

![bg fit](https://images.ctfassets.net/w1bd7cq683kz/5Ex6830HzBPU5h8Ou8xQAB/2c948105fc10094348203bec6c1eab04/Kubernetes_20architecture_20diagram.png)

---
# What is GitOps?  
- GitOps is a way of implementing Continuous Deployment for cloud native applications, it uses Git as a source of truth for declarative infrastructure and application code.

- It uses a pipeline to automatically deploy changes and bring the system to the desired state, defined in a Git repository, and continuously monitors the cluster for drift.

- GitOps also facilitates collaboration, traceability, and rollbacks by using version control in the Git repository.

![bg left:10% 80%](https://www.almtoolbox.com/blog/wp-content/uploads//2022/03/gitops.png)

---
# Why use Gitops?

- Automation and Efficiency

- Collaboration and traceability

- Security 

- Scalability 

- Flexibility 

- Reliability

- Speed 

- Cost-effective

![bg left:10% 80%](https://www.almtoolbox.com/blog/wp-content/uploads//2022/03/gitops.png)

----
# How GitOps Works?
- GitOps uses a Git repository to store the desired state of the system and a pipeline to continuously monitor and update the system to match that desired state.

- The pipeline includes automated tests and security checks, and can monitor the cluster for drift and automatically correct it.

- GitOps facilitates collaboration and traceability, and allows for easy rollbacks by using version control in the Git repository.

---
![bg fit ](https://www.cncf.io/wp-content/uploads/2022/08/image1-31.png)

---
# What is Crossplane?
Crossplane is an open-source multi-cloud control plane that enables users to manage infrastructure as code and automate provisioning, scaling, and management of cloud resources. It provides a common way to provision and manage resources across different cloud providers and can be integrated with Kubernetes.

![bg left:10% 80%](https://cncf-branding.netlify.app/img/projects/crossplane/icon/color/crossplane-icon-color.png)

---
# Why use Crossplane?

- Crossplane allows you to manage cloud resources using the same tools and workflows that you use to manage your Kubernetes clusters.

- Crossplane enables users to provision and manage cloud resources from different providers using a common set of APIs and tools, reducing the complexity of multi-cloud deployments.

- Crossplane enables users to define, compose, and manage reusable infrastructure as code, allowing for more efficient and consistent deployments.

![bg left:10% 80%](https://cncf-branding.netlify.app/img/projects/crossplane/icon/color/crossplane-icon-color.png)

---
# How Crossplane works?
- Crossplane uses a Kubernetes-native API to provision and manage cloud resources, making it easy to integrate with existing Kubernetes workflows and tools.

- Crossplane uses a Custom Resource Definition (CRD) to define the desired state of cloud resources, which can be versioned and tracked in Git.

---
# How Crossplane works?
- Crossplane uses controllers that watch for changes to the CRDs and automatically provision and manage the resources to match the desired state.

- Crossplane can be integrated with other Kubernetes tools such as Helm, Kustomize, and Kubernetes Operators to provide a powerful and flexible multi-cloud infrastructure management solution.
---
#
![bg fit](https://freecontent.manning.com/wp-content/uploads/defining-infrastructure-declaratively-with-crossplane_01.png)

---