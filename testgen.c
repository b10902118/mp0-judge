#include "kernel/types.h"

#include "kernel/fcntl.h"
#include "kernel/stat.h"
#include <kernel/fs.h>
#include "user/user.h"

#define BUFSZ 58

void mkfile(char *filename) {
    int fd = open(filename, O_CREATE | O_RDWR);
    write(fd, "hi", 3);
    close(fd);
}

void mkd(char *dirname) {
    if (mkdir(dirname) < 0) {
        fprintf(2, "mkdir %s failed.", dirname);
        exit(1);
    }
}

#include "test.c"

void rm_rf(char *path) {
    // printf("%s\n", path);
    int cur = open(path, 0);
    if (cur < 0) {
        printf("Error open %s\n", path);
        return;
    }

    struct stat st;
    struct dirent de;

    while (read(cur, &de, sizeof(de)) == sizeof(de)) {
        if (de.inum == 0 || strcmp(de.name, ".") == 0 ||
            strcmp(de.name, "..") == 0)
            continue;
        else {
            char buf[BUFSZ] = "";
            strcpy(buf, path);
            int path_len = strlen(path);
            buf[path_len] = '/';
            strcpy(buf + path_len + 1, de.name);
            // printf("%s\n", buf);
            stat(buf, &st);
            switch (st.type) {
            case T_FILE:
                if (strcmp(path, ".") != 0) unlink(buf);
                break;

            case T_DIR:
                // printf("%s is dir\n", buf);
                rm_rf(buf);
                break;
            }
        }
    }
    close(cur);
    if (strcmp(path, ".") != 0) unlink(path);
}

int main(int argc, char *argv[]) {
    rm_rf(".");
    test();
    exit(0);
}
