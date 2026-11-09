// 03_tests.inc - shared tests for 03_exercises.cpp and 03_solutions.cpp (do not edit)
#include <cmath>
#include <cstdio>

static int g_pass = 0, g_total = 0;
#define CHECK(name, cond)                                                     \
    do {                                                                      \
        g_total++;                                                            \
        if (cond) { g_pass++; std::printf("  PASS  %s\n", name); }            \
        else { std::printf("  FAIL  %s\n", name); }                           \
    } while (0)

static bool near(float a, float b, float tol = 1e-3f) { return std::fabs(a - b) <= tol; }

int main() {
    CHECK("1 counts_to_g: +/-2 g range, 16384 counts = 1 g", near(counts_to_g(16384, 2), 1.0f));
    CHECK("1 counts_to_g: +/-8 g range, 4096 counts = 1 g", near(counts_to_g(4096, 8), 1.0f));
    CHECK("1 counts_to_g: negative values", near(counts_to_g(-8192, 2), -0.5f));

    CHECK("2 is_clipped: 32767 is clipped", is_clipped(32767));
    CHECK("2 is_clipped: -32768 is clipped", is_clipped(-32768));
    CHECK("2 is_clipped: 16000 is fine", !is_clipped(16000));

    CHECK("3 windows: 10 s @1 kHz, 2 s window, 0.2 s stride = 41", windows_in_recording(10000, 2000, 200) == 41);
    CHECK("3 windows: no overlap = 5", windows_in_recording(10000, 2000, 2000) == 5);
    CHECK("3 windows: recording shorter than window = 0", windows_in_recording(1500, 2000, 200) == 0);

    const float inter[] = {1, 10, 100, 2, 20, 200, 3, 30, 300};
    float x[3], y[3], z[3];
    deinterleave(inter, 3, x, y, z);
    CHECK("4 deinterleave: x axis", x[0] == 1 && x[1] == 2 && x[2] == 3);
    CHECK("4 deinterleave: z axis", z[0] == 100 && z[1] == 200 && z[2] == 300);

    const float sq[] = {1, -1, 1, -1};
    const float three[] = {3, 4};
    CHECK("5 rms: square wave of +/-1 = 1", near(rms(sq, 4), 1.0f));
    CHECK("5 rms: {3, 4} = 3.5355", near(rms(three, 2), 3.5355f));

    MovingAverage ma;
    ma_init(&ma);
    float out = 0;
    for (int i = 0; i < 4; i++) out = ma_update(&ma, 8.0f);
    CHECK("6 moving average: partly filled buffer averages what it has", near(out, 8.0f));
    for (int i = 0; i < 8; i++) out = ma_update(&ma, (i % 2) ? 1.0f : -1.0f);
    CHECK("6 moving average: removes +/-1 alternating noise", near(out, 0.0f));
    for (int i = 0; i < 8; i++) out = ma_update(&ma, 5.0f);
    CHECK("6 moving average: settles on a constant", near(out, 5.0f));

    std::printf("\n%d/%d passed\n", g_pass, g_total);
    return g_pass == g_total ? 0 : 1;
}
