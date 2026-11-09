// 02_int8_quantization.cpp
//
// What float32 -> int8 quantization actually does, in ~60 lines.
//
// Compile & run:
//   python -m ziglang c++ -std=c++11 -O2 02_int8_quantization.cpp -o 02.exe && 02.exe
//
// The idea:
//   int8 has only 256 levels (-128..127). We map the float range [min, max] onto them:
//       scale      = (max - min) / 255
//       zero_point = -128 - round(min / scale)
//       q          = clamp(round(x / scale) + zero_point, -128, 127)     // store: 1 byte
//       x_back     = (q - zero_point) * scale                            // use: approximate
//   Each step is `scale` wide. Anything smaller than one step is lost.

#include <cmath>
#include <cstdint>
#include <cstdio>

struct QParams { float scale; int32_t zero_point; };

static QParams choose_params(const float *x, int n) {
    float lo = x[0], hi = x[0];
    for (int i = 1; i < n; i++) { if (x[i] < lo) lo = x[i]; if (x[i] > hi) hi = x[i]; }
    if (lo > 0) lo = 0;                                  // range must include 0
    if (hi < 0) hi = 0;
    QParams p;
    p.scale = (hi - lo) / 255.0f;
    p.zero_point = -128 - (int32_t)std::lround(lo / p.scale);
    return p;
}

static int8_t quantize(float x, QParams p) {
    long q = std::lround(x / p.scale) + p.zero_point;
    if (q > 127) q = 127;
    if (q < -128) q = -128;
    return (int8_t)q;
}

static float dequantize(int8_t q, QParams p) { return (q - p.zero_point) * p.scale; }

static void demo(const char *title, const float *x, int n) {
    QParams p = choose_params(x, n);
    std::printf("\n%s\n  scale (step size) = %.5f, zero_point = %d\n", title, p.scale, (int)p.zero_point);
    std::printf("  %10s %6s %10s %8s\n", "float32", "int8", "back", "error");
    for (int i = 0; i < n; i++) {
        int8_t q = quantize(x[i], p);
        float b = dequantize(q, p);
        std::printf("  %10.4f %6d %10.4f %8.4f\n", x[i], (int)q, b, b - x[i]);
    }
}

int main() {
    // Typical, well-behaved feature values
    const float good[] = {-1.20f, -0.51f, -0.50f, 0.00f, 0.02f, 0.03f, 0.49f, 1.15f};
    demo("1) Normal range: errors are tiny compared with the values", good, 8);

    // Same values plus ONE outlier (e.g. a sensor glitch that got into the training data)
    const float outlier[] = {-1.20f, -0.51f, -0.50f, 0.00f, 0.02f, 0.03f, 0.49f, 60.0f};
    demo("2) One outlier stretches the range: small values collapse into the same step", outlier, 8);

    const int N = 100000;  // e.g. weights of a small model
    std::printf("\nMemory for %d values: float32 = %d KB, int8 = %d KB (4x smaller)\n",
                N, (int)(N * sizeof(float) / 1024), (int)(N * sizeof(int8_t) / 1024));
    return 0;
}

/* TRY THIS:
   1. In demo 2, which values became identical? That is the "lost detail".
   2. Remove the outlier but change 1.15 to 5.0. How big is the step now?
   3. Customer line: "int8 is like saving a photo as JPEG: 4x smaller, usually looks the
      same - and Studio shows float32 vs int8 accuracy side by side, so we check."
*/
