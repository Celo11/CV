// 03_solutions.cpp - reference answers for 03_exercises.cpp (try first!)
//   python -m ziglang c++ -std=c++11 -O2 03_solutions.cpp -o 03s.exe && 03s.exe

#include <cmath>
#include <cstdint>

float counts_to_g(int16_t counts, int range_g) {
    const float counts_per_g = 32768.0f / (float)range_g;
    return (float)counts / counts_per_g;
}

bool is_clipped(int16_t counts) {
    return counts == INT16_MAX || counts == INT16_MIN;
}

uint32_t windows_in_recording(uint32_t n_samples, uint32_t window, uint32_t stride) {
    if (n_samples < window || stride == 0) return 0;   // check BEFORE subtracting (unsigned)
    return (n_samples - window) / stride + 1;
}

void deinterleave(const float *in, uint32_t n_samples, float *x, float *y, float *z) {
    for (uint32_t i = 0; i < n_samples; i++) {
        x[i] = in[3 * i + 0];
        y[i] = in[3 * i + 1];
        z[i] = in[3 * i + 2];
    }
}

float rms(const float *x, uint32_t n) {
    if (n == 0) return 0.0f;
    float sum_sq = 0.0f;
    for (uint32_t i = 0; i < n; i++) sum_sq += x[i] * x[i];
    return std::sqrt(sum_sq / (float)n);
}

struct MovingAverage {
    float buf[8];
    uint8_t idx;
    uint8_t count;
    float sum;
};

void ma_init(MovingAverage *m) {
    for (int i = 0; i < 8; i++) m->buf[i] = 0.0f;
    m->idx = 0;
    m->count = 0;
    m->sum = 0.0f;
}

float ma_update(MovingAverage *m, float x) {
    m->sum -= m->buf[m->idx];        // value leaving the window (0 while still filling)
    m->buf[m->idx] = x;
    m->sum += x;
    m->idx = (uint8_t)((m->idx + 1) % 8);
    if (m->count < 8) m->count++;
    return m->sum / (float)m->count;
}

#include "03_tests.inc"
