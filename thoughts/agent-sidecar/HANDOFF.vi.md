# Bàn giao Agent Sidecar 0.1.0

**Ngày:** 17/11/2026. **Trạng thái:** source implementation + local tests hoàn thành;
chờ người dùng review/nghiệm thu. Chưa tạo repo, commit, push hoặc deploy.

## Kiến trúc giữ nguyên

**Agent Kit — Quyết định & quản trị -> Sidecar — Thực thi & tối ưu.**
Sidecar nằm ở repository độc lập. Gói Agent Kit V2 đầu vào không bị sửa.
Không nhúng Swamp, không cần tài khoản Swamp, không tích hợp LLM vào runtime.

## Đã triển khai

| Phần | Kết quả |
| --- | --- |
| Giao việc nguyên khối | `delegate` nhận một work package đã có quyền, tự chạy DAG rồi trả một terminal result |
| Registry | YAML/JSON, schema chặt, dependency/cycle checks, workflow/version/digest pin |
| Admission | Policy allowlist, request-bound local permit, expiry, runtime/policy/snapshot checks |
| Snapshot | Content digest cho source chưa commit/untracked; công bố exclusions; không dùng HEAD thay source thực tế |
| Executor | Builtin read-only và process chỉ dành cho trusted code khi cho phép riêng |
| Điều phối | Dependencies, concurrency, success/always condition, timeouts, cancellation, retry có điều kiện |
| Bằng chứng | PASS/FAIL/NOT_RUN, artifact hashes, byte caps, unknown effects và escalation |
| Lịch sử | Atomic run records, inspect/history, chống chạy trùng cùng request ID |
| Phối hợp V2 | Giữ nguyên ba schema 0.1.0, validator semantics; hướng dẫn gọi ngoài repo |

Không chỉ chạy test cuối task: `repo.prepare` kiểm kê source và trích xuất entrypoints
trước khi Coding Agent cần suy luận. Hai workflow còn lại kiểm tra integrity và chạy
bốn lệnh verification gốc của V2. Sidecar không điều khiển business reasoning hay
cho phép deploy/sửa production.

## Kết quả kiểm tra đã quan sát

**105/105 bài kiểm thử Sidecar PASS, không skipped.** Cả ba workflow chạy thực tế thành
công. `agentkit.verify` chạy đủ bốn lệnh, gồm **77 tests của V2 PASS**. Chính validator
gốc của V2 chấp nhận cả ba bộ request/result/capability thật. Gói V2 gốc không thay đổi.
Wheel build và CLI từ wheel đã được kiểm tra. Xem [báo cáo](docs/VERIFICATION.md) và log.

Những con số này không phải benchmark tiết kiệm token và không phải nghiệm thu của bạn.

## Lựa chọn runtime

Bản này dùng **Python 3.11+**, `jsonschema==4.26.0`, `PyYAML==6.0.3`. Go trước đó là đề
xuất, chưa chốt stack; runtime hiện tại dùng trực tiếp canonical JSON/validator đã có
ở V2, thay vì tạo thêm dialect hoặc bộ kiểm tra schema riêng. Không có engine Go.

## Các giới hạn phải giữ rõ

**Chưa có sandbox OS/network.** Builtin không chạy code dự án; process mode chỉ được
bật cho code/host tin cậy. Private copy và process group không ngăn code độc hại truy
cập host/network. Không dùng cho untrusted PR hay production cần cách ly cứng.

Chưa kiểm thử native Codex/Claude/Gemini/Cursor hoặc trên máy Mac của bạn. Host đã
kiểm thử là Linux + Python 3.13.5. Chưa có scheduler, distributed workers, tự resume
sau crash, workflow mining, cache tổng quát hoặc số liệu token tiết kiệm thực tế.
Process step không dùng chung thư mục build output với step khác.

Giấy phép/approval metadata không cấp quyền. Same-request replay protection không
ngăn hai request ID mới đại diện cùng ý định: mất response thì inspect trước, không
lặp `delegate` vô thức. Unknown effects phải reconcile trước khi chạy tiếp.

## Cách tiếp nhận

Giải nén, đọc [README](README.md), [hướng dẫn VI](docs/START-HERE.vi.md) và
[SECURITY](SECURITY.md). Kiểm tra source/registry/policy, cài dependency trong môi trường
bạn cho phép rồi chạy ví dụ synthetic read-only. Source ZIP không có `.git`, credentials,
snapshots hoặc runtime working copies. File bằng chứng đi kèm chỉ là lịch sử kiểm thử.

Bạn có thể tạo repository mới và tự commit sau khi review. Không có bước Git tự động.
