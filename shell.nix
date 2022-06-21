with import <nixpkgs> {};

mkShell {
  buildInputs = [
    act
    pre-commit
    git-crypt
    detect-secrets
  ];
}
