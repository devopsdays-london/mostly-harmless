with import <nixpkgs> {};

mkShell {
  buildInputs = [
    act
    pre-commit
    shellcheck
    git-crypt
  ];
}
