from collections import deque
st=deque()
st.append(0)
st.appendleft(1)
st.append(2)
st.popleft()
print(st)