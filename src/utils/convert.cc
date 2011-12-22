#include "utils/convert.h"
#include <iconv.h>

int code_convert(char *from_charset, char *to_charset, 
        char *src, size_t nSrc, char *dst, size_t nDst) {
    iconv_t id;
    int rc;

    id = iconv_open(to_charset, from_charset);
    if (id == 0)
        return -1;
//    memset(dst, 0, nDst);

    if (iconv(id, &src, &nSrc, &dst, &nDst) == -1) {
        return -1;
    }

    iconv_close(id);

    return 0;
}

int g2u(char *src, int nSrc, char *dst, int nDst) {
    return code_convert("gb2312", "utf-8", src, nSrc, dst, nDst);
}
