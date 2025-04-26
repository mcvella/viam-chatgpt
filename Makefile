.PHONY: build run test test-individual coverage install-test-deps

build:
	sh build.sh
run:
	./dist/main