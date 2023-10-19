import py_vncorenlp
import os


# Automatically download VnCoreNLP components from the original repository
# and save them in some local working folder
py_vncorenlp.download_model(save_dir='/VnCoreNLP/models')

# Load VnCoreNLP from the local working folder that contains both `VnCoreNLP-1.2.jar` and `models` 
# model = py_vncorenlp.VnCoreNLP(save_dir='/home/trantrongtien_qt/VnCoreNLP/models')


rdrsegmenter = py_vncorenlp.VnCoreNLP(annotators=["wseg"], save_dir='/VnCoreNLP/models')
text = "Ông Nguyễn Khắc Chúc  đang làm việc tại Đại học Quốc gia Hà Nội. Bà Lan, vợ ông Chúc, cũng làm việc tại đây."
text_v1 = '''
    Hoài nghi về số thương vong trong vụ nổ bệnh viện Gaza

Các cơ quan tình báo châu Âu cho rằng số người chết trong vụ nổ tại bệnh viện Al-Ahli thấp hơn nhiều so với thống kê được Hamas công bố.

"Không phải 200 hay 500 người chết trong vụ nổ, nhiều khả năng số nạn nhân thiệt mạng là khoảng 10-50", AFP hôm 18/10 dẫn nguồn tin từ các cơ quan tình báo châu Âu, đề cập đến tổn thất về người trong vụ tập kích bệnh viện Al-Ahli, miền trung Dải Gaza một ngày trước đó.

WSJ cùng ngày dẫn nhận định từ một số nhà phân tích cho rằng phạm vi nhỏ ở khu vực xảy ra vụ nổ trong sân bệnh Al-Ahli, cùng tác động không lớn từ sóng xung kích không thể gây ra thương vong lớn như giới chức Hamas công bố.

Một vụ nổ lớn xảy ra tại bệnh viện Al-Ahli đêm 17/10. Hamas ban đầu thông báo 200-300 người chết, sau đó nâng số nạn nhân thiệt mạng lên ít nhất 500 người. Đến ngày 18/10, lực lượng này sửa con số thống kê thành ít nhất 471 người chết, đồng thời cáo buộc quân đội Israel ném bom vào bệnh viện.

Tuy nhiên, nhà phân tích thông tin tình báo Blake Spendley nói rằng các video, hình ảnh hiện trường cho thấy vụ nổ tại bệnh viện Al-Ahli chỉ có thể khiến 50 người thiệt mạng, ít hơn nhiều so với số liệu được Hamas công bố.

Hình ảnh hiện trường vụ nổ cho thấy miệng hố va chạm trên sân bệnh viện tương đối nông, các tòa nhà trong khuôn viên cơ sở y tế này cũng không chịu thiệt hại lớn, với các tấm năng lượng mặt trời lắp trên mái còn nguyên vẹn, cho thấy luồng sóng xung kích tạo ra không mạnh.
Miệng hố tương đối nông ở sân bệnh viện Al-Ahli sau vụ tập kích đêm 17/10. Ảnh: X/@Osinttechnical

Miệng hố tương đối nông ở sân bệnh viện Al-Ahli sau vụ tập kích đêm 17/10. Ảnh: X/@Osinttechnical

Israel khẳng định nước này không tấn công bệnh viện Al-Ahli và cho rằng một quả rocket của tổ chức Jihad Hồi giáo Palestine (PIJ) đã gặp sự cố sau khi phóng và rơi xuống sân bệnh viện.

Theo quân đội Israel, đầu đạn của rocket kết hợp với thuốc phóng chưa cháy hết đã tạo ra vụ nổ và đám cháy, nhưng động năng của quả đạn rơi xuống không lớn nên không khoét hố sâu trên mặt đất. Trong khi đó, bom hoặc tên lửa do Israel sử dụng trong các cuộc không kích thường tạo ra miệng hố có đường kính 7-19 mét trên mặt đất.

Người phát ngôn Hội đồng An ninh Quốc gia Mỹ Adrienne Watson cho biết dựa vào phân tích hình ảnh vệ tinh cùng các nguồn tin tình báo, Washington cho rằng Israel không thực hiện vụ tấn công bệnh viện Al-Ahli. Tổng thống Mỹ Joe Biden cũng nói rằng ông tin Israel không gây ra sự việc.

Các quan chức Mỹ cho hay tình báo nước này đã thu thập dữ liệu vệ tinh và hồng ngoại cho thấy rocket gây ra vụ nổ bệnh viện được phóng từ vị trí của các lực lượng vũ trang bên trong Dải Gaza.
    '''
output = rdrsegmenter.word_segment(text_v1)
print(output)
