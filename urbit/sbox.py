# forward 255-sbox
zaft = [None, 186, 87, 38, 39, 145, 213, 253, 43, 15, 27, 26, 72, 130, 193, 136, 92, 222, 42, 233, 189, 12, 123, 108, 59, 210, 158, 218, 251, 10, 208, 118, 101, 239, 137, 221, 68, 241, 110, 80, 55, 214, 62, 64, 40, 122, 71, 34, 155, 76, 142, 8, 44, 170, 148, 25, 152, 37, 184, 164, 216, 79, 86, 9, 230, 156, 95, 57, 153, 132, 151, 21, 63, 32, 191, 224, 93, 116, 149, 254, 168, 242, 231, 60, 139, 181, 234, 75, 157, 243, 182, 91, 138, 113, 140, 206, 226, 85, 107, 109, 211, 228, 198, 23, 255, 131, 172, 50, 28, 48, 127, 114, 3, 83, 17, 250, 150, 248, 135, 195, 144, 125, 1, 14, 196, 185, 183, 119, 197, 175, 88, 94, 215, 236, 69, 201, 120, 4, 103, 178, 6, 41, 2, 180, 82, 235, 166, 165, 190, 207, 67, 36, 11, 129, 187, 98, 53, 61, 143, 13, 147, 35, 227, 58, 73, 52, 84, 238, 237, 96, 167, 77, 19, 51, 106, 104, 219, 212, 171, 209, 99, 49, 173, 225, 29, 24, 115, 112, 203, 78, 54, 159, 163, 176, 247, 22, 90, 46, 161, 97, 245, 249, 102, 223, 111, 162, 220, 74, 31, 56, 128, 194, 89, 244, 217, 105, 141, 20, 169, 100, 124, 232, 7, 70, 18, 45, 199, 5, 16, 174, 81, 133, 126, 192, 252, 229, 205, 65, 30, 246, 33, 202, 146, 160, 121, 179, 240, 66, 154, 177, 47, 200, 134, 188, 117, 204]
# forward 256-sbox
zyft = [225, 158, 250, 151, 39, 212, 50, 182, 51, 143, 223, 30, 104, 144, 63, 217, 220, 156, 57, 5, 54, 80, 139, 207, 189, 111, 132, 70, 35, 185, 193, 112, 244, 38, 11, 55, 103, 141, 29, 253, 33, 109, 133, 245, 173, 9, 157, 85, 237, 49, 59, 15, 168, 246, 94, 208, 170, 53, 214, 177, 42, 166, 82, 44, 227, 16, 188, 209, 197, 58, 110, 233, 234, 43, 34, 135, 178, 12, 86, 149, 128, 83, 163, 252, 41, 243, 8, 64, 27, 179, 216, 191, 215, 78, 10, 18, 91, 21, 203, 231, 194, 99, 115, 52, 162, 150, 164, 190, 130, 20, 251, 84, 26, 230, 161, 175, 72, 66, 24, 210, 69, 201, 148, 117, 241, 226, 88, 7, 229, 76, 0, 98, 171, 127, 145, 147, 153, 97, 136, 247, 154, 167, 195, 249, 19, 142, 90, 89, 46, 4, 81, 137, 242, 102, 125, 235, 79, 123, 205, 255, 159, 36, 119, 3, 202, 222, 40, 200, 108, 238, 240, 74, 32, 61, 67, 65, 236, 68, 121, 100, 92, 126, 172, 218, 198, 138, 116, 122, 14, 206, 114, 56, 211, 101, 62, 37, 192, 1, 174, 60, 254, 239, 28, 47, 199, 196, 232, 248, 140, 118, 106, 152, 45, 77, 6, 87, 186, 120, 204, 160, 48, 224, 155, 13, 93, 96, 146, 176, 169, 25, 213, 75, 113, 131, 165, 124, 219, 221, 95, 17, 71, 22, 181, 105, 134, 107, 228, 23, 2, 180, 129, 184, 31, 183, 73, 187]
# reverse 255-sbox
zart = [None] * 256
for i,x in enumerate(zaft[1:]):
    zart[x] = i + 1
# reverse 256-sbox
zyrt = [None] * 256
for i,x in enumerate(zyft):
    zyrt[x] = i
