def Quicksort(arr,l,h):
    if l<h:
        p_i=partition(arr,l,h)
        Quicksort(arr ,l,p_i-1)
        Quicksort(arr,p_i+1,h)
def partition(arr,l,h):
    p_e=arr[h]
        