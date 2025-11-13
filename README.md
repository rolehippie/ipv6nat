# ipv6nat

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/ipv6nat)
[![General Workflow](https://github.com/rolehippie/ipv6nat/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/ipv6nat/actions/workflows/general.yml)
[![Readme Workflow](https://github.com/rolehippie/ipv6nat/actions/workflows/docs.yml/badge.svg)](https://github.com/rolehippie/ipv6nat/actions/workflows/docs.yml)
[![Galaxy Workflow](https://github.com/rolehippie/ipv6nat/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/ipv6nat/actions/workflows/galaxy.yml)
[![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/ipv6nat)](https://github.com/rolehippie/ipv6nat/blob/master/LICENSE)
[![Ansible Role](https://img.shields.io/badge/role-rolehippie.ipv6nat-blue)](https://galaxy.ansible.com/rolehippie/ipv6nat)

Ansible role to install and configure ipv6nat.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of contents

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [ipv6nat_download](#ipv6nat_download)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.10`

## Default Variables

### ipv6nat_download

Download URL for ipv6nat binary

#### Default value

```YAML
ipv6nat_download: 
  https://github.com/robbertkl/docker-ipv6nat/releases/download/v0.4.0/docker-ipv6nat.amd64
```

## Discovered Tags

**_ipv6nat_**

## Dependencies

- None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
