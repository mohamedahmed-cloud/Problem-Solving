#include <stdio.h>
#include <pthread.h>

int value = 10;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

void *runner(void *param);

int main(int argc, char *argv[]) {
    pthread_t tid;
    pthread_attr_t attr;
    printf("%d\n", value); /* LINE A */
    pthread_attr_init(&attr);
    pthread_create(&tid, &attr, runner, NULL);
    pthread_join(tid, NULL);
    printf("%d\n", value); /* LINE B */
    pthread_mutex_destroy(&mutex);
    return 0;
}

void *runner(void *param) {
    pthread_mutex_lock(&mutex);
    value = 5;
    pthread_mutex_unlock(&mutex);
    pthread_exit(0);
}