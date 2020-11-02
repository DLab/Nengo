import imageio


class im:
	def resize(img,n):
	    temp = Image.open(img)
	    x,y=temp.size
	    size=[x/n,y/n]
	    temp.thumbnail(size)
	    temp_1 = np.asarray(temp)
	    #im = Image.fromarray(a)
	    return (temp_1)