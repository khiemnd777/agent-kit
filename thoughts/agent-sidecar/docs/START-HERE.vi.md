# Bắt đầu với Agent Sidecar 0.1.0

**Agent Kit quản trị/quyết định. Sidecar thực thi/tối ưu.** Hai repository độc lập;
bản này không sửa gói Agent Kit V2, không tạo repo GitHub và không commit/push.

## Đây là phần mềm chạy thật

Runtime dùng **Python 3.11+**, JSON Schema và YAML. Go trong trao đổi trước là đề xuất;
bản này dùng trực tiếp cách tính request digest và validator Python đã bàn giao ở V2.
Không có Swamp dependency, tài khoản, API key, LLM gateway hay dịch vụ nền.

Cài trong môi trường bạn cho phép theo README. Không có script tự cài dependency.
Ví dụ read-only hoàn chỉnh nằm ở mục “A real one-call delegation” trong README.

## WHEN và một lần giao việc

Ngay khi gặp một nhóm công việc ổn định đã được cho phép, Coding Agent chọn DELEGATE.
Không phải đợi viết code xong: `repo.prepare` có thể chạy trước khi điều tra/lập kế hoạch.
`sidecar delegate` nhận capability, source, inputs, scope và decision reference; tự
snapshot/pin/kiểm tra quyền, chạy toàn bộ DAG rồi trả một kết quả.

Đây không phải Agent gọi từng lệnh inventory, đọc output, quyết định bước tiếp theo,
gọi manifest và lặp lại. Các bước nội bộ do code của Sidecar điều phối. Agent chỉ cần
xử lý mục tiêu, quyền hạn, bằng chứng cần đọc và ngoại lệ.

`--confirm-authorized` chỉ ghi nhận **quyền đã có thật**. Nó không tạo ra quyền mới,
không chứng minh có người thật đã phê duyệt và không thay thế permission của coding
client/OS. Policy phải được review trước. Không thêm một vòng xin duyệt cho từng step.

## Ba workflow có sẵn

| Workflow | Công việc | Chế độ |
| --- | --- | --- |
| `repo.prepare` | Kiểm kê source snapshot, hash file, đọc entrypoints khai báo trong manifest | Builtin, không chạy code dự án |
| `agentkit.integrity` | So hash manifest và skill mirror của V2 | Builtin; không thay toàn bộ verification |
| `agentkit.verify` | Chạy bốn lệnh kiểm tra gốc của V2 theo dependencies | Process; chỉ source/tool đã tin cậy và được cho phép |

Một command/script/CI đơn giản đã đủ thì dùng DIRECT. Business logic mới, thiết kế
kiến trúc và lỗi chưa biết nguyên nhân vẫn cần REASON; Sidecar không làm thay.

## Kiểm thử source

```sh
python3 tools/verify.py --out /tmp/sidecar-evidence
```

Kiểm tra với gói Agent Kit V2 thật, chỉ sau khi đã review source đó:

```sh
python3 tools/interop.py \
  --agent-kit /duong-dan/agent-kit-v2 \
  --out /tmp/sidecar-v2-interop \
  --confirm-trusted-code
```

Chọn output mới. Script tạo snapshot và chạy trên bản sao; sau đó dùng chính
`scripts/check_contract.py` trong V2 để kiểm tra request/result/capability thực tế.
Không tạo commit, không sửa V2 nguồn, không mở ứng dụng Codex/Claude.

## Giới hạn cần biết

**Chưa có sandbox OS/network.** Process mode mặc định bị chặn; bật lên đồng nghĩa
chỉ chạy code tin cậy trên host tin cậy. Bản sao riêng không ngăn code độc hại truy
cập hệ thống. Không dùng cho untrusted PR, production, dữ liệu khách hàng hoặc thao
tác cần cách ly cứng. Không có scheduler, distributed workers hay tự resume sau crash.

Khi bị ngắt/timeout, đọc effects_state và reconcile trước khi chạy lại. `run` với
cùng request ID không thực thi lại kết quả đã xong; gọi `delegate` mới tạo intent mới.
Khi mất response, đọc history/result trước, không gọi delegate lặp vô thức.

Báo cáo token của Coding Agent chưa được đo. Builtin không gọi LLM; process có usage
không biết thì ghi null. PASS runtime không phải nghiệm thu của bạn.

Đọc tiếp: [Hướng dẫn phối hợp V2](AGENT-KIT-INTEGRATION.md), [WHEN](WHEN.md),
[Security](../SECURITY.md), [Bàn giao](../HANDOFF.vi.md).
