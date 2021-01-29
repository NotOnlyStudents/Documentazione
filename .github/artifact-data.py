import sys
import json

def main():
    matrix = json.loads("".join(sys.argv[1:]));

    working_directories = [ m["working_directory"].split("/") for m in matrix["include"] ]

    common_path = 0;

    for i in range(1, min([len(working_directory) for working_directory in working_directories])):
        equal = True

        for j in range(len(working_directories) - 1):
            equal = equal and working_directories[j][i] == working_directories[j + 1][i]

        if not equal:
            break

        common_path = i

    if common_path == 0:
        artifact_name = "Documentazione"
        artifact_path = "."
    else:
	    artifact_name = working_directories[0][common_path];
	    artifact_path = '/'.join(working_directories[0][1:common_path + 1]);
	    
    artifact = { "name": artifact_name, "path": artifact_path }

    print(json.dumps(artifact))

if __name__ == "__main__":
    main();
