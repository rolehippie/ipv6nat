# ipv6nat

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/ipv6nat) [![Build Status](https://img.shields.io/drone/build/rolehippie/ipv6nat/master?logo=drone)](https://cloud.drone.io/rolehippie/ipv6nat) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/ipv6nat)](https://github.com/rolehippie/ipv6nat/blob/master/LICENSE) 

Ansible role to install and configure ipv6nat. 

## Sponsor 

[![Proact Deutschland GmbH](https://proact.eu/wp-content/uploads/2020/03/proact-logo.png)](https://proact.eu) 

Building and improving this Ansible role have been sponsored by my employer **Proact Deutschland GmbH**.

## Table of content

* [Default Variables](#default-variables)
  * [ipv6nat_download](#ipv6nat_download)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

---

## Default Variables

### ipv6nat_download

Download URL for ipv6nat binary

#### Default value

```YAML
ipv6nat_download: https://github.com/robbertkl/docker-ipv6nat/releases/download/v0.4.0/docker-ipv6nat.amd64
```

## Dependencies

* [rolehippie.docker](https://github.com/rolehippie/docker)

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
