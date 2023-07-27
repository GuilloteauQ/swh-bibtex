{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/23.05";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in
    {
      apps.${system} = rec{
        default = swh-bibtex;
        swh-bibtex = {
          type = "app";
          program = "${self.packages.${system}.default}/bin/swh-bibtex";
        };
      };
      packages.${system} = rec {
        default = swh-bibtex;
        swh-bibtex = pkgs.python3Packages.buildPythonPackage {
          name = "swh-bibtex";
          version = "0.0.1";
          src = ./.;
          propagatedBuildInputs = with (pkgs.python3Packages); [
            requests
          ];
          doCheck = false;
        };      
      };
      devShells.${system}.default = with pkgs;
        mkShell {
          packages = [ python3 python3Packages.requests ];
        };
    };
}
