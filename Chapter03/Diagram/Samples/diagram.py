from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from urllib.request import urlretrieve

with Diagram("Introduction", show=True, filename="Introduction", direction="LR"):

  # download the icon image file
  diagrams_url = "https://media.licdn.com/dms/image/C4E03AQGP0cPFJDEK6A/profile-displayphoto-shrink_400_400/0/1641394473152?e=1679529600&v=beta&t=ZN80bsqQrbM9nx5DhosdbuzoqPxNOYko714Kp_Xggc0"
  diagrams_icon = "diagrams.png"
  urlretrieve(diagrams_url, diagrams_icon)

  diagrams = Custom("Ebrahim Ramadan", diagrams_icon)

  with Cluster("Certifications and Experience"):

    openstack_url = ""
    openstack_icon = "openstack.png"
    urlretrieve(openstack_url, openstack_icon)

    openstack = Custom("OpenStack", openstack_icon)

    elastic_url = "https://github.com/mingrammer/diagrams/raw/master/resources/elastic/saas/elastic.png"
    elastic_icon = "elastic.png"
    urlretrieve(elastic_url, elastic_icon)

    elastic = Custom("Elastic", elastic_icon)

  diagrams >> openstack
  diagrams >> elastic