import os
import time 
import py_vncorenlp



class Segmentation:
    def __init__(self) -> None:
        cwd = os.getcwd()
        self.model_dir = os.path.join(cwd, config("MODEL_DIR", cast=str))
        self.rdrsegmenter = py_vncorenlp.VnCoreNLP(annotators=["wseg"], save_dir=self.model_dir)
    
    
    def preprocess_data(self, data):
        res = []
        for d in data:
            temps = d.split(' ')
            for t in temps:
                if t not in res:
                    temp_str = t.replace('_', ' ')
                    if check_if_match_vietnamese(temp_str):
                        res.append(temp_str)
        
        return res
    
    def segmentation_file(self, file_path):
        f = open(file_path, "r")
        file_content = f.read()
        return self.segmentation_text(file_content)

    
    def segmentation_text(self, text):
        output = self.rdrsegmenter.word_segment(text)

        res = self.preprocess_data(output)

        # add to queue for updating db
        put_msgs_to_queue(res, QUEUE_DB_WRITER)

        return res
    


def main():
    seg = Segmentation()

    start_time = time.time()
    text = "Nhận được tin, ngay sáng 29-9, Đồn Biên phòng Nậm Càn, Bộ đội Biên phòng Nghệ An đã cử lực lượng phối hợp cùng dân quân địa phương hai xã Lưu Phong, Tương Dương và Nậm Càn, Kỳ Sơn kịp thời có mặt xúc đất, chặt cây,... giải tỏa giao thông cho người dân đi lại. Đến 9 giờ 30 phút sáng nay giao thông đã được đảm bảo thông suốt."
    text1 = "Sáng 26/9, tại trụ sở Bộ Quốc phòng, Đại tướng Lương Cường - Ủy viên Bộ Chính trị, Chủ nhiệm Tổng cục Chính trị Quân đội nhân dân Việt Nam chủ trì lễ đón Đoàn đại biểu chính trị cấp cao Quân đội nhân dân Lào thăm chính thức Việt Nam từ ngày 25 đến ngày 28/9/2023. Ngay sau lễ đón, Đại tướng Lương Cường và Thượng tướng Thongloi Silivong đồng chủ trì hội đàm giữa hai đoàn."
    text2 = "Cụ thể tuyến đường tỉnh 543D Lưu Kiền Na Ngoi qua địa bàn xã Nậm Càn, huyện Kỳ Sơn bị sạt lở, làm ách tắc giao thông, các phương tiện qua lại đoạn đường này tạm thời bị gián đoạn."
    text3 = "Duy chỉ có 1 chỗ, đó chính là TTCK sẽ phản ánh trước, đi trước khoảng từ 3-6 tháng. ACE còn tò mò về việc phản ánh trước thì có thể đọc lại bài viết trước đây của Châu trên 24hmoney."
    text_4 = '''
    Bệnh viện ở Dải Gaza bị tập kích, ít nhất 500 người chết

Hamas nói quân đội Israel tập kích một bệnh viện ở miền trung Dải Gaza, khiến ít nhất 500 người thiệt mạng, nhưng Tel Aviv bác bỏ cáo buộc.

Văn phòng truyền thông của chính quyền Hamas ở Gaza cáo buộc Israel đêm 18/10 tấn công vào sân bệnh viện Al-Ahli ở miền trung Dải Gaza, mô tả sự việc là một "tội ác chiến tranh".

"Ít nhất 500 người đã thiệt mạng trong đợt tập kích", giới chức Hamas cho hay. "Hàng trăm nạn nhân mắc kẹt dưới đống đổ nát". Trước đó, lực lượng này nói rằng 200-300 người đã chết.

Hình ảnh hiện trường từ Al Jazeera cho thấy các nhân viên y tế và dân thường đang thu thập thi thể bằng túi màu trắng hoặc chăn trong bóng tối. Sân bệnh viện đầy vết máu và ôtô bị thiêu rụi.

Bệnh viện là nơi nhiều người phải sơ tán vì xung đột ở Dải Gaza tìm đến trú ẩn, bởi những cơ sở này hầu như không bị nhắm đến khi quân đội Israel tập kích đáp trả Hamas.

Israel bác cáo buộc cho rằng quân đội nước này đã đánh trúng Al-Ahli.
Người dân Palestine đưa một em bé bị thương trong vụ tập kích bệnh viện Ahli Arab ngày 17/10 đến bệnh viện al-Shifa ở Gaza City, Dải Gaza. Ảnh: Reuters

Người dân Palestine đưa một em bé bị thương trong vụ tập kích bệnh viện Al-Ahli ngày 17/10 đến bệnh viện Al-Shifa ở Gaza City, Dải Gaza. Ảnh: Reuters

"Toàn thế giới nên biết rằng chính những kẻ khủng bố tàn bạo ở Gaza đã tấn công bệnh viện, không phải Lực lượng Phòng vệ Israel (IDF)", Thủ tướng Israel Benjamin Netanyahu nói. "Họ sát hại tàn bạo trẻ em của chúng tôi, và cũng sát hại trẻ em của chính họ".

Người phát ngôn IDF cho biết phân tích từ hệ thống tác chiến cho thấy một loạt rocket "được những kẻ khủng bố ở Dải Gaza phóng đã bay qua khu vực gần Al-Ahli vào thời điểm bệnh viện trúng đòn". Quân đội Israel cáo buộc thủ phạm là nhóm cực đoan Jihad Hồi giáo Palestine (PIJ), đồng minh của Hamas.

"Chúng tôi có thông tin tình báo từ nhiều nguồn chứng minh các phần tử Thánh chiến Hồi giáo chịu trách nhiệm về vụ phóng rocket thất bại và đánh trúng bệnh viện ở Gaza", người này nói.

PIJ bác bỏ cáo buộc từ Israel, nói thông tin từ IDF là "những lời dối trá".

Tổng thống Palestine Mamoud Abbas ngày 18/10 mô tả sự việc là "vụ thảm sát chiến tranh ghê tởm" không thể tha thứ. "Israel đã vượt lằn ranh đỏ... Chúng tôi sẽ không rời đi hay cho phép bất kỳ ai trục xuất chúng tôi khỏi khu vực", ông Abbas bổ sung.

Tổng thống Mỹ Joe Biden gửi lời chia buồn về tổn thất sinh mạng trong sự việc, chúc những người bị thương sớm bình phục. Ông chủ Nhà Trắng dự kiến đến Israel hôm nay để thể hiện sự ủng hộ dành cho nước này.

Cao ủy về nhân quyền Liên Hợp Quốc Volker Turk lên án vụ tập kích bệnh viện, gọi đây là hành động không thể chấp nhận được. "Dân thường phải được bảo vệ, hỗ trợ nhân đạo phải được phép tiếp cận những người đang cần sự giúp đỡ", ông nói.

Chủ tịch Hội đồng châu Âu (EC) Charles Michel nói tấn công vào hạ tầng dân sự là vi phạm luật pháp quốc tế. Quan chức phụ trách đối ngoại của Liên minh châu Âu (EU) Josep Borrell cho biết thông tin bệnh viện Al-Ahli bị tập kích "làm gia tăng sự kinh hoàng của thảm kịch đang diễn ra trước mắt chúng ta suốt nhiều ngày qua".

Nga, Anh, Pháp, Ai Cập cùng một số quốc gia, tổ chức khác cũng lên án vụ tập kích bệnh viện Al-Ahli. Nga và Các tiểu vương quốc Arab Thống nhất đã kêu gọi Hội đồng Bảo an Liên Hợp Quốc họp khẩn trong ngày 18/10.
Vị trí bệnh viện Al-Alhi. Đồ họa: Middle East Eye

Vị trí bệnh viện Al-Alhi. Đồ họa: Middle East Eye

Quân đội Israel không kích Dải Gaza từ 7/10 để đáp trả cuộc tấn công bất ngờ của Hamas cùng ngày trước đó. Tính đến ngày 17/10, giao tranh giữa hai bên đã khiến khoảng 4.400 người thiệt mạng, ít nhất 16.000 người bị thương.

Israel đã bao vây hoàn toàn Gaza, cắt nguồn cung điện, lương thực và nhiên liệu. Dải Gaza là nơi có 2,3 triệu dân Palestine sinh sống, vốn phụ thuộc vào các nguồn tiếp tế từ bên ngoài qua lãnh thổ Israel. Israel ngày 13/10 yêu cầu 1,1 triệu dân thường ở miền bắc Dải Gaza sơ tán về phía nam, trong bối cảnh IDF chuẩn bị mở chiến dịch quân sự vào khu vực.
    '''

    text_5 = '''
    Krông Pắc (còn được viết là Krông Pắk) là một huyện thuộc tỉnh Đắk Lắk, Việt Nam.

Tên huyện theo chữ Êđê là Krông Pač (đọc là cờ-rông pách) chữ "č" (c có dấu á (ă) tương tự chữ ch trong tiếng Việt), ví dụ Cư Huê là Čư Huê (Čư là núi).[2] Tên gọi này được đặt theo tên của sông Krông Pắc, một trong hai phụ lưu hợp thành của sông Krông Ana, đồng thời là phụ lưu cấp 2 của sông Sêrêpôk.
Địa lý

Huyện Krông Pắc nằm ở phía đông tỉnh Đắk Lắk, có vị trí địa lý:

    Phía đông giáp huyện Ea Kar
    Phía tây giáp thành phố Buôn Ma Thuột
    Phía tây bắc giáp huyện Cư M'gar
    Phía nam giáp huyện Krông Bông
    Phía tây nam giáp huyện Cư Kuin
    Phía bắc giáp thị xã Buôn Hồ.

Huyện Krông Pắc có diện tích 625,81 km², dân số năm 2017 là 207.226 người, gồm các dân tộc: Kinh, Êđê, Tày, Nùng, M'nông, Vân kiều, H'Mông... Trong đó dân tộc Kinh chiếm khoảng 65%.
Hành chính

Huyện Krông Pắc có 16 đơn vị hành chính cấp xã trực thuộc, bao gồm thị trấn Phước An (huyện lỵ) và 15 xã: Ea Hiu, Ea Kênh, Ea Kly, Ea Knuếc, Ea Kuăng, Ea Phê, Ea Uy, Ea Yiêng, Ea Yông, Hòa An, Hòa Đông, Hòa Tiến, Krông Búk, Tân Tiến, Vụ Bổn.
Lịch sử

Năm 1923, tỉnh Darlac được thành lập và được đặt dưới quyền cai trị của một công sứ Pháp. Ban đầu, dưới chính quyền cấp tỉnh không phân thành các cấp hành chính như ở miền xuôi, mà chỉ có các tòa đại lý hành chính quản lý theo vùng. Mãi đến năm 1931, Toàn quyền Đông Dương ra nghị định thành lập đơn vị hành chính cấp quận ở các tỉnh Tây Nguyên, tương tự như các quận ở Nam Kỳ. Tỉnh Darlac gồm 5 quận: Buôn Mê Thuộc, Buôn Hồ, Lăk, Đăk Song, M'Đrăk, với 440 buôn làng.

Nghị định số 356-BNV/HC/NĐ của chính quyền Việt Nam Cộng hòa ngày 2 tháng 7 năm 1958 ấn định tỉnh Darlac có 5 quận, 21 tổng và 77 xã. Trong đó, quận Ban Mê Thuột có 4 tổng, quận Lạc Thiện (đổi tên từ quận Lăk) có 7 tổng, quận M’Đrak có 4 tổng, quận Đak Song có 2 tổng và quận Buôn Hồ có 4 tổng.

Năm 1959, quận M'Đrak bị giải thể. Trong đó, 2 tổng Krong Hinh và Krong Jing được sáp nhập vào tỉnh Khánh Hòa để thành lập quận Khánh Dương thuộc tỉnh Khánh Hòa, còn 2 tổng Ea Bar và Krong Pa được sáp nhập vào tỉnh Phú Yên để thành lập quận Phú Đức thuộc tỉnh Phú Yên.

Sau năm 1975, quận Phước An sáp nhập với quận Khánh Dương (thuộc tỉnh Khánh Hòa) thành huyện Krông Pắc, gồm 19 xã: Cư Kty, Ea Bhốk, Ea Kar, Ea Knuếc, Ea Kuăng, Ea Ktur, Ea Trang, Ea Trul, Ea Yiêng, Ea Yông, Hòa An, Hòa Hiệp, Hòa Lễ, Hòa Sơn, Hòa Tiến, Khuê Ngọc Điền, Krông Bông, Krông Búk và Krông Jing.

Ngày 30 tháng 8 năm 1977, Hội đồng Chính phủ ban hành Quyết định 230-CP[3]. Theo đó, tách 2 xã: Krông Jing và Ea Trang để thành lập huyện M'Drắk.

Huyện Krông Pắc còn lại 17 xã.

Ngày 20 tháng 4 năm 1978, thành lập 3 xã: Hòa Thành, Hòa Tân và Hòa Phong.[4]

Ngày 17 tháng 9 năm 1981, chia xã Ea Yiêng thành 2 xã: Ea Yiêng và Ea Uy.[5]

Ngày 19 tháng 9 năm 1981, Hội đồng Bộ trưởng ban hành Quyết định 75-HĐBT[6]. Theo đó:

    Tách 3 xã: Ea Bhôk, Ea Ktur và Hòa Hiệp để thành lập huyện Krông Ana (nay 3 xã này thuộc huyện Cư Kuin)
    Tách 9 xã: Cư Kty, Ea Trul, Hòa Lễ, Hòa Phong, Hòa Sơn, Hòa Tân, Hòa Thành, Khuê Ngọc Điền và Krông Bông để thành lập huyện Krông Bông.

Huyện Krông Pắc còn lại 9 xã: Ea Kar, Ea Knuếc, Ea Kuăng, Ea Uy, Ea Yiêng, Ea Yông, Hòa An, Hòa Tiến và Krông Búk.

Ngày 12 tháng 11 năm 1983, chia xã Ea Kuăng thành 3 xã: Ea Kuăng, Ea Phê và Ea Hiu.[7]

Ngày 13 tháng 9 năm 1986, Hội đồng Bộ trưởng ban hành Quyết định 108-HĐBT[8]. Theo đó, chuyển xã Ea Kar về huyện Ea Kar mới thành lập.

Huyện Krông Pắc còn lại 10 xã: Ea Hiu, Ea Knuếc, Ea Kuăng, Ea Phê, Ea Uy, Ea Yiêng, Ea Yông, Hòa An, Hòa Tiến và Krông Búk.

Trong giai đoạn 1988-1994, huyện thành lập thêm 3 đơn vị hành chính: thị trấn Krông Pắc và 2 xã Ea Kênh, Tân Tiến.

Ngày 21 tháng 1 năm 1995, Chính phủ ban hành Nghị định 08/CP[9]. Theo đó, chuyển xã Hòa Đông thuộc thành phố Buôn Ma Thuột về huyện Krông Pắc quản lý.

Ngày 18 tháng 11 năm 1996, Chính phủ ban hành Nghị định 71-CP[10]. Theo đó:

    Chia xã Krông Búk thành 3 xã: Krông Búk, Ea Kly và Vụ Bổn
    Đổi tên thị trấn Krông Pắc thành thị trấn Phước An.

Ngày 26 tháng 11 năm 2003, Quốc hội ban hành Nghị quyết 22/2003/QH11 chia tỉnh Đắk Lắk thành hai tỉnh: Đắk Lắk và Đắk Nông[11], huyện Krông Pắc thuộc tỉnh Đắk Lăk, bao gồm 1 thị trấn và 15 xã như hiện nay.

Ngày 30 tháng 8 năm 2012, Bộ Xây dựng ban hành Quyết định 800/QĐ-BXD về việc công nhận thị trấn Phước An là đô thị loại IV.[12]
Kinh tế - xã hội
Kinh tế

Huyện có thế mạnh là diện tích đất đỏ Bazan để phát triển cây cà phê. Đây là một trong những nơi đầu tiên được du nhập cây cà phê với đồn điền Ca Da do người Pháp xây dựng.
Giáo dục

Huyện Krông Pắk có ngành giáo dục phát triển mạnh với 23 trường mẫu giáo mầm non, 51 trường tiểu học, 24 trường trung học cơ sở trực thuộc Phòng Giáo dục.
Du lịch
Trên địa bàn huyện có Thiền viện Trúc Lâm Từ Giác đang trong giai đoạn thi công. 
    '''
    # print(seg.segmentation_text(text))
    # print(seg.segmentation_text(text1))
    # print(seg.segmentation_text(text2))
    # print(seg.segmentation_text(text3))
    # print(seg.segmentation_text(text_4))
    # print(seg.segmentation_text(text_5))
    # stop_time = time.time()
    # print(f"Time executed: {round(stop_time-start_time, 2)}")
    print(seg.segmentation_file("/mnt/Projects/TeleLog/core/VnCoreNLP/test.txt"))

if __name__ == "__main__":
    main()



