#include "utils/convert.h"
#include <iconv.h>
#include <string.h>

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
    return code_convert("gbk", "utf-8//IGNORE", src, nSrc, dst, nDst);
}

char dec2char(int val) {
    if (val >= 0 && val <= 9) {
        return (char)(val + '0');
    } else if (val >= 10 && val <= 15) {
        return (char)(val - 10 + 'A');
    } else {
        return 0;
    }
}

void utf2url(char *pUtf, char *pUrl) {
    int nLen = strlen(pUtf);
    char *p = pUrl;
    int j, i;
    for (i = 0, j = 0; i < nLen; i++) {
        char c = pUtf[i];
        if ((c >= '0' && c <= '9') || (c >= 'a' && c <= 'z') ||
            (c >= 'A' && c <= 'Z') || c == '/' || c == '.' || 
            c == '_' || c == '-') {
            p[j++] = c;
        } else {
            int val = (int)c;
            if (val < 0) {
                val += 256;
            }
            int ih, il;
            ih = val / 16;
            il = val - ih * 16;

            p[j++] = '%';
            p[j++] = dec2char(ih);
            p[j++] = dec2char(il);
        }
    }

    p[j] = 0;
}
