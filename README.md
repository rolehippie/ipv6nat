# ipv6nat

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/ipv6nat) [![Testing Build](https://github.com/rolehippie/ipv6nat/workflows/testing/badge.svg)](https://github.com/rolehippie/ipv6nat/actions?query=workflow%3Atesting) [![Readme Build](https://github.com/rolehippie/ipv6nat/workflows/readme/badge.svg)](https://github.com/rolehippie/ipv6nat/actions?query=workflow%3Areadme) [![Galaxy Build](https://github.com/rolehippie/ipv6nat/workflows/galaxy/badge.svg)](https://github.com/rolehippie/ipv6nat/actions?query=workflow%3Agalaxy) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/ipv6nat)](https://github.com/rolehippie/ipv6nat/blob/master/LICENSE)

Ansible role to install and configure ipv6nat.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Default Variables](#default-variables)
  - [ipv6nat_download](#ipv6nat_download)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Default Variables

### ipv6nat_download

Download URL for ipv6nat binary

#### Default value

```YAML
ipv6nat_download: https://github.com/robbertkl/docker-ipv6nat/releases/download/v0.4.0/docker-ipv6nat.amd64
```

## Discovered Tags

**_ipv6nat_**


## Dependencies

- [rolehippie.docker](https://github.com/rolehippie/docker)

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
