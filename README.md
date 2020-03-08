# ipv6nat

[![Build Status](https://cloud.drone.io/api/badges/rolehippie/ipv6nat/status.svg)](https://cloud.drone.io/rolehippie/ipv6nat)

Ansible role to configure ipv6nat

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

* [docker](https://github.com/rolehippie/docker)

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
