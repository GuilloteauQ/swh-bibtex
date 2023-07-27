# swh-bibtex

Generate a bibtex entry for a git repository archived on Software Heritage


## Run

```bash
nix run github:guilloteauq/shw-bibtex -- <URL>
```

The `<URL>` is the one from your git provider (github, gitlab, etc.).

## Example


```bash
$ nix run github:guilloteauq/shw-bibtex -- https://github.com/oar-team/oar3 https://gitlab.inria.fr/qguillot/batsim.jl

@software{oar3,
    name = {oar3},
    author = {oar-team},
    url = {https://github.com/oar-team/oar3},
    year = {2023},
    swhid = {swh:1:dir:ab502da78090e4d77ee363ce7ccc2f6ea65c2d92;origin=https://github.com/oar-team/oar3;}
}


@software{batsim.jl,
    name = {batsim.jl},
    author = {qguillot},
    url = {https://gitlab.inria.fr/qguillot/batsim.jl},
    year = {2023},
    swhid = {swh:1:dir:9b11d1efa57ea3ea8a1023e39b3b863cdd6e4145;origin=https://gitlab.inria.fr/qguillot/batsim.jl;}
}
```
