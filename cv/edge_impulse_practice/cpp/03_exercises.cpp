// 03_exercises.cpp - microcontroller-style C++ exercises
//
// Fill in each TODO, then compile & run:
//   python -m ziglang c++ -std=c++11 -O2 03_exercises.cpp -o 03.exe && 03.exe
// (Any C++ compiler works: g++, clang++, or an online one like godbolt.org / onlinegdb.com
//  - paste this file and the contents of 03_tests.inc together.)
//
// Rules, as on a real microcontroller:
//   - no new / malloc / std::vector: fixed-size arrays only
//   - use fixed-width types (int16_t, uint32_t)
//   - every function should run in a predictable amount of time

#include <cmath>
#include <cstdint>

// 1. Raw counts -> g.
//    A 16-bit accelerometer reports -32768..32767. On the +/-range_g setting,
//    32768 counts = range_g, so counts_per_g = 32768 / range_g.
//    (+/-2 g -> 16384 counts per g, +/-8 g -> 4096 counts per g)
float counts_to_g(int16_t counts, int range_g) {
    // TODO
    (void)counts; (void)range_g;
    return 0.0f;
}

// 2. Has this reading hit the sensor's limit (saturated)?
bool is_clipped(int16_t counts) {
    // TODO
    (void)counts;
    return false;
}

// 3. How many windows does a recording give? (the "41 windows" question)
//    0 if the recording is shorter than one window.
uint32_t windows_in_recording(uint32_t n_samples, uint32_t window, uint32_t stride) {
    // TODO  careful: unsigned maths! n_samples - window wraps around if n_samples < window
    (void)n_samples; (void)window; (void)stride;
    return 0;
}

// 4. Split an interleaved buffer [x0, y0, z0, x1, y1, z1, ...] into three arrays.
void deinterleave(const float *in, uint32_t n_samples, float *x, float *y, float *z) {
    // TODO
    (void)in; (void)n_samples; (void)x; (void)y; (void)z;
}

// 5. Root mean square: sqrt( (x0^2 + x1^2 + ...) / n )
float rms(const float *x, uint32_t n) {
    // TODO  (std::sqrt is in <cmath>)
    (void)x; (void)n;
    return 0.0f;
}

// 6. Moving average over the last 8 values, the classic MCU noise filter.
//    Do it in O(1): keep a running sum; add the new value, subtract the one leaving.
//    Before 8 values have arrived, average only the values you have.
struct MovingAverage {
    float buf[8];
    uint8_t idx;     // where the next value goes
    uint8_t count;   // how many values stored so far (max 8)
    float sum;       // running sum of the values in buf
};

void ma_init(MovingAverage *m) {
    // TODO  set everything to zero
    (void)m;
}

float ma_update(MovingAverage *m, float x) {
    // TODO
    (void)m; (void)x;
    return 0.0f;
}

#include "03_tests.inc"
