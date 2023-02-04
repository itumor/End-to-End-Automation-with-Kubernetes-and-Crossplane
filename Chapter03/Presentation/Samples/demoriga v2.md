---
marp: true
theme: gaia
_class: lead
paginate: true 
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
size: 16:9

---
# GitOpsifying Cloud Infra with Crossplane
---
# About Me
- Ebrahim Ramadan Cloud Architect at Accenture Baltics

- Certifications: CKA CKAD KCNA SAA

- Core Skills: AWS Kubernetes Docker Istio.io GitOps CI/CD Crossplane

- Experience: 13 years of experience in the computer software industry Worked with 5 companies 22 projects

---

# Introduction

- Problem
- Solution
- Kubernetes
- Argo CD
- Crossplane
- What Why How Crossplane? 
- Crossplane Concepts.
- Demo 
- Q & A 
- Thanks


---

# Problem
 The problem is to achieve **true GitOps** for both **infrastructure** and applications while minimizing the use of **multiple tools** and **languages** and reducing **complexity**. 

---
# solution
- Kubernetes and Argo CD, along with Crossplane, are solutions that help to solve the problem statement by providing a more streamlined and automated approach to managing infrastructure and applications using GitOps principles.

----
# Kubernetes

Kubernetes provides a platform for deploying, scaling, and managing containerized applications, making it easier to manage infrastructure as code.

![bg left:10% 80%](https://kubernetes.io/images/favicon.png)

---
# Argo CD

 Argo CD is a GitOps-based continuous delivery tool that automates the deployment of applications to Kubernetes clusters, helping to ensure that the desired state of the infrastructure is always in sync with the state described in Git.

![bg left:10% 80%](https://cncf-branding.netlify.app/img/projects/argo/stacked/color/argo-stacked-color.png)

---
# Crossplane
 Crossplane provides a unified control plane that makes it easier to manage multiple cloud resources using GitOps principles, by allowing administrators to manage infrastructure as code.

![bg left:10% 80%](https://cncf-branding.netlify.app/img/projects/crossplane/icon/color/crossplane-icon-color.png)

---
- By combining these tools, it becomes possible to achieve true GitOps for both infrastructure and applications, reducing complexity and minimizing the need to use multiple tools and languages.
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

![bg left:10% 80%](https://cncf-branding.netlify.app/img/projects/crossplane/icon/color/crossplane-icon-color.png)

---
# How Crossplane works?
- Crossplane uses controllers that watch for changes to the CRDs and automatically provision and manage the resources to match the desired state.

- Crossplane can be integrated with other Kubernetes tools such as Helm, Kustomize, and Kubernetes Operators to provide a powerful and flexible multi-cloud infrastructure management solution.

![bg left:10% 80%](https://cncf-branding.netlify.app/img/projects/crossplane/icon/color/crossplane-icon-color.png)

---
#
![bg fit](https://raw.githubusercontent.com/itumor/End-to-End-Automation-with-Kubernetes-and-Crossplane/46e8007ac954926a642c37c70e0af13e06f24de7/Chapter03/Presentation/Samples/images/crossplane1.png)

---
# Crossplane Concepts
- Providers
- Managed Resources (MR)
- Composite Resources (XRs)
- Composite Resource Definition (XRD)
- Composite 
- Composite Resource Claim (Claim)
- How Composite Resources Works 


---
# Providers
Providers are Crossplane packages that bundle a set of Managed Resources and their respective controllers to allow Crossplane to provision the respective infrastructure resource.

![bg right fit](https://blog.codecentric.de/_next/image?url=https%3A%2F%2Fmedia.graphassets.com%2Foutput%3Dformat%3Awebp%2FWAtrV4JRB64mnqOFNQKA&w=3840&q=75)

---
```yaml
apiVersion: pkg.crossplane.io/v1
kind: Provider
metadata:
  name: provider-aws
spec:
  package: "xpkg.upbound.io/crossplane-contrib/provider-aws:v0.33.0"
```
```yaml
apiVersion: aws.crossplane.io/v1beta1
kind: ProviderConfig
metadata:
  name: aws-provider
spec:
  credentials:
    source: Secret
    secretRef:
      namespace: crossplane-system
      name: aws-creds
      key: creds
```
---
# Managed Resources
is Crossplane’s representation of a resource in an external system  most commonly a cloud. Managed Resources are opinionated, Crossplane Resource Model (XRM) compliant Kubernetes Custom Resources that are installed by a Crossplane provider.

![bg right fit](https://freecontent.manning.com/wp-content/uploads/defining-infrastructure-declaratively-with-crossplane_05.png)

---
```yaml
apiVersion: database.aws.crossplane.io/v1beta1
kind: RDSInstance
metadata:
  name: rdspostgresql
spec:
  forProvider:
    region: us-east-1
    dbInstanceClass: db.t2.small
    masterUsername: masteruser
    allocatedStorage: 20
    engine: postgres
    engineVersion: "12"
    skipFinalSnapshotBeforeDeletion: true
  writeConnectionSecretToRef:
    namespace: crossplane-system
    name: aws-rdspostgresql-conn
```
---
# Composite Resources
Crossplane Composite Resources are opinionated Kubernetes Custom Resources that are composed of Managed Resources. We often call them XRs for short.

![bg right fit](https://docs.crossplane.io/media/composition-xrs-and-mrs.svg)

---
#  Composite Resource Definition 
Composite Resource Definitions (XRDs) are modelled on similar Kubernetes concepts - Custom Resources (CRs) and Custom Resource Definitions (CRDs).

---
```YAML
apiVersion: apiextensions.crossplane.io/v1
kind: CompositeResourceDefinition
metadata:
  name: xpostgresqlinstances.database.example.org
spec:
  group: database.example.org
  names:
    kind: XPostgreSQLInstance
    plural: xpostgresqlinstances
  claimNames:
    kind: PostgreSQLInstance
    plural: postgresqlinstances
  versions:
  - name: v1alpha1
    served: true
    referenceable: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            properties:
              parameters:
                type: object
                properties:
                  storageGB:
                    type: integer
                required:
                - storageGB
            required:
            - parameters

```
---

# Composition
Composition in Crossplane refers to the process of composing multiple underlying resources into a higher-level abstraction

---
```yaml
apiVersion: apiextensions.crossplane.io/v1
kind: Composition
metadata:
  name: example
  labels:
    crossplane.io/xrd: xpostgresqlinstances.database.example.org
    provider: gcp
spec:
  writeConnectionSecretsToNamespace: crossplane-system
  compositeTypeRef:
    apiVersion: database.example.org/v1alpha1
    kind: XPostgreSQLInstance
  resources:
  - name: cloudsqlinstance
    base:
      apiVersion: database.gcp.crossplane.io/v1beta1
      kind: CloudSQLInstance
      spec:
        forProvider:
          databaseVersion: POSTGRES_12
          region: us-central1
          settings:
            tier: db-custom-1-3840
            dataDiskType: PD_SSD
            ipConfiguration:
              ipv4Enabled: true
              authorizedNetworks:
                - value: "0.0.0.0/0"
    patches:
    - type: FromCompositeFieldPath
      fromFieldPath: spec.parameters.storageGB
      toFieldPath: spec.forProvider.settings.dataDiskSizeGb
```
---
# Composite Resource Claim
A “Composite Resource Claim”, “XRC”, or just “a claim” is also an API type defined using Crossplane. Each type of claim corresponds to a type of composite resource, and the pair have nearly identical schemas. Like composite resources, the type of a claim is arbitrary.

---
```yaml
apiVersion: database.example.org/v1alpha1
kind: PostgreSQLInstance
metadata:
  namespace: default
  name: my-db
spec:
  parameters:
    storageGB: 20
  compositionRef:
    name: production
  writeConnectionSecretToRef:
    name: my-db-connection-details
```
---
# How Composite Resources Works 

![bg fit 50% ](https://docs.crossplane.io/media/composition-how-it-works.svg)

---
# Demo



---
![bg fit ](https://www.michaelleestallard.com/wp-content/uploads/qa-760x406.jpg)

---
You Can Find Me https://www.linkedin.com/in/Ebrahim-Ramadan

![bg fit ](https://englishlive.ef.com/blog/wp-content/uploads/sites/2/2015/05/thank-you.jpg)

![bg fit 80% ](https://chart.googleapis.com/chart?cht=qr&chl=https%3A%2F%2Fwww.linkedin.com%2Fin%2FEbrahim-Ramadan%2F&chs=180x180&choe=UTF-8&chld=L|2)


