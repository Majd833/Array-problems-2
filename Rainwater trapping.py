# program to fing the amount of water that we can trap within a given set of bars.
def find(a,asize):
    #make an array to hold the height of left tallest bar for any ith bar
    left=[0]*asize
    #make an array to hold the height of right tallest bar for any ith bar
    right=[0]*asize
    #initialize result
    water =0
    #fill left array
    left[0]=a[0]
    for i in range (1,asize):
        left[i]=max(left[i-1],a[i])
    #fill right array
    right[0]=a[0]
    for i in range (1,asize):
        left[i]=max(right[i-1],a[i])
    #Water trapped for any ith bar should be minimum of the left and right heighest bar-bar height
    for i in range(0,asize):
        water+=min(left[i],right[i]-a[i])
    return water
a=[0,1,0,2,1,0,1,3,2,1,2,1]
bars=len(a)
print(find(a,bars))