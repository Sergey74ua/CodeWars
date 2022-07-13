// Локально не запускал

char* number_to_string(int number) {
    char* c;
    asprintf(&c, "%d", number);
    return c;
}