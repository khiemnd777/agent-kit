# Bàn giao Agent Kit V2

**Phiên bản nguồn:** 2.0.0 — chờ bạn review/nghiệm thu.
**Ngày:** 17/11/2026.
**Ranh giới:** Chỉ Agent Kit. Dừng trước Sidecar; không tạo repo, commit, push, PR,
merge, deploy hoặc áp dụng sang dự án khác.

## Kiến trúc đã hiện thực ở lớp Agent Kit

**Agent Kit — Quyết định và quản trị → Sidecar — Thực thi và tối ưu.**

Agent Kit V2 vẫn là instructions, skills và adapter cho Coding Agent, không phải
một tiến trình. Bản này thay đổi cách Agent chọn và giao việc: giao cả nhóm việc
có quy trình ổn định vào đúng thời điểm; chỉ quay lại reasoning khi cần quyết định,
phân tích hoặc xử lý ngoại lệ. Không giới hạn automation ở bước test cuối cùng.

Sidecar chưa được xây. Khi chưa có executor thật, Agent dùng lệnh/script/CI sẵn
có trong phạm vi được duyệt hoặc báo thiếu điều kiện. Không có CLI Sidecar giả,
runner, scheduler, registry service, hay cơ chế tự cài đặt.

## Những phần đã làm

| Hạng mục | Kết quả |
| --- | --- |
| Operating core | Viết lại AGENTS.md theo Decision & Governance |
| Quyết định WHEN | DIRECT / DELEGATE / REASON / WAIT, dùng ở đầu task hoặc một nhóm việc ổn định giữa task |
| Approval | Giữ phê duyệt kế hoạch, scope, human stops và acceptance; không hỏi lại từng bước đã được duyệt |
| Reporting | Bỏ biểu mẫu WHAT/skills-percentage/journal/visual bắt buộc cho mọi tác vụ nhỏ |
| Skills | 17 tên kỹ năng hiện có được thích ứng cho V2; thêm execution-delegation |
| Mirrors và adapter | Mirror Claude đồng bộ; 3 vai trò × 4 client = 12 adapter nguồn |
| Giao tiếp tương lai | 3 JSON Schemas dạng draft 0.1.0, 8 ví dụ dữ liệu giả lập, validator ngoại tuyến |
| Bằng chứng | Kiểm tra request/snapshot, required checks, artifacts, kết quả không rõ, số đo thiếu và giới hạn output |
| Kiểm tra package | Inventory/hash, license, local links, frontmatter/TOML, mirror, export và unit tests |
| Hướng dẫn | Migration, acceptance, benchmark A/B/C, provenance và bản tham chiếu Grok |

**Contract và ví dụ không phải Sidecar chạy thật.** Metadata quyền hạn không cấp
quyền; JSON Schema không phải sandbox. Các ví dụ PASS/FAIL đều ghi synthetic.

## Kết quả kiểm tra

77 bài kiểm thử tự động đã đạt trong môi trường tạo package. Các kiểm tra cấu
trúc package, mirror/adapter, 3 schemas, ví dụ và bản export đều đạt. Chi tiết và
log được ghi tại `docs/verification-results.md` và `docs/delivery/`.

Chưa kiểm thử native discovery/invocation/quyền thực tế trên Codex, Claude Code,
Gemini, Cursor hay Grok. Chưa có benchmark token/latency và chưa có kiểm thử
interoperability với Sidecar. Không dùng việc giảm chữ trong tài liệu để tuyên bố
đã giảm token khi chạy task thật.

## Nguồn và thay đổi bố cục

Đọc nguồn V1 tại commit `df3b058a52acc9ea10a7556733baae44ac12d1f2` bằng GitHub connector.
Đây là bản V2 tái cấu trúc có chọn lọc, không phải archive đầy đủ V1. Các hướng dẫn
dài được cô đọng; lịch sử task/phê duyệt V1 không được mang sang thành quyền mới.
Giấy phép MIT và attribution gốc được giữ; không sao chép source Swamp.

Các file `docs/project-context.md`, `project-plan.md`, `project-state.md` là template
UNINITIALIZED cho dự án áp dụng sau này, không chứa nghiệm thu giả.

## Bạn tự đưa lên repository mới

Giải nén, đọc README và `docs/START-HERE.vi.md`, rồi review mã nguồn/tài liệu.
Thư mục có cả các thư mục ẩn `.agents`, `.claude`, `.codex`, `.gemini`, `.cursor`;
không có `.git` hay credential. Các lệnh kiểm tra nằm trong README; không có bước
auto-upload. Việc bạn tạo repo và commit là bước riêng do bạn thực hiện.

**Dừng tại Agent Kit V2. Sidecar chưa triển khai.**
