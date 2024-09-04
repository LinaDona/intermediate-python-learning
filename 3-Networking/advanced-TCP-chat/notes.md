# `recv`
`recv` throws an exception if an error occurred. Closing a socket by the peer is no error, but is a normal behavior. In fact it is not even a full close: the peer only indicates that it will not send any more data, but it might still receive data. The TCP connection is only closed if both sides indicate that they will not send any more data, i.e. each side has send the FIN.

# sockets and OSs
Nothing happens immediatly over the network. That's one thing.

Secondly the underlying OS will detect broken connections (and Python gets that info in the form of an exception), but usually this takes time. And that's why you still send messages even though the connection is already dead. But since OS operates on network layer (as opposed to the application layer) then there's an issue: the connection may be dead but OS may never detect this. For example this will happen when the server is dead but behind alive proxy.

Thirdly the most reliable way to know that a server is alive is when it sends something back to the client. So you should always .recv() (with timeout) after .sendall() call and the server should always .sendall() after .recv() (the request-response pattern, even when the response is a simple "I received message"). If you can't modify the server side and (in worst case) if the server doesn't send anything back to the client then there's no reliable way to know this.

That's why you need some form of framing/correctness protocol. Simple .sendall() won't do.