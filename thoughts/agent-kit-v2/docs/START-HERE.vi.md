# Bắt đầu với Agent Kit V2

## Bản này làm gì?

Agent Kit V2 là lớp **Quyết định và quản trị** cho Coding Agent. Nó xác định mục
tiêu, phạm vi, quyền hạn, tiêu chí nghiệm thu và thời điểm giao cả nhóm việc lặp
lại cho công cụ thực thi. Agent không cần quyết định lại từng bước đã biết trước.

Sidecar là dự án độc lập ở giai đoạn sau. Bản này **không chứa Sidecar**, không
chạy ngầm, không theo dõi Codex và không tự kết nối dịch vụ nào.

## Dùng ngay, chưa cần Sidecar

Mở thư mục này trong Coding Agent; giao một công việc cụ thể. Agent đọc
`AGENTS.md`, lập kế hoạch phù hợp và tôn trọng phê duyệt của bạn. Các công việc
cơ học dùng lệnh/script/CI đã có. Công việc mới dùng reasoning. Không giả định
Sidecar đã tồn tại hoặc tự cài thêm runtime.

Khi đưa vào dự án đã có, cần xem các rules/skills hiện tại và duyệt phạm vi áp
dụng; không chép đè toàn bộ hoặc mang theo phê duyệt của dự án khác.

## Bốn lựa chọn

- DIRECT: lệnh/script/CI hiện có đã đủ.
- DELEGATE: có executor thật, đã được kiểm tra và được cấp quyền cho đúng nhóm việc.
- REASON: cần phân tích, thiết kế, lập trình hoặc điều tra nguyên nhân.
- WAIT: thiếu quyền, quyết định quan trọng, điều kiện an toàn hoặc có yêu cầu dừng.

Đây là policy của Agent, không phải một router đang chạy trong máy.

## Kiểm tra trước khi bạn tự commit

Chạy bốn lệnh trong README. Công cụ kiểm tra chỉ kiểm tra package, mirror,
contracts và tài liệu; không chạy workflow, không gọi LLM, không truy cập GitHub.
Xem `docs/verification-results.md` để phân biệt kết quả đã chạy và NOT_RUN.

Bạn tự tạo repository và commit gói này. Không có `.git`, remote, token hay
credential trong gói. `docs/delivery/V2-BUILD.md` ghi rõ ranh giới đã bàn giao.
Phần Sidecar dừng ở tài liệu/hợp đồng dự thảo, chưa triển khai runtime.
