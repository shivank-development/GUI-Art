import pydicom
import matplotlib.pyplot as plt

# Load sample DICOM file
ds = pydicom.dcmread(
    pydicom.data.get_testdata_file("CT_small.dcm")
)

# Display image
plt.imshow(ds.pixel_array, cmap="gray")
plt.title("CT Slice")
plt.axis("off")
plt.show()
