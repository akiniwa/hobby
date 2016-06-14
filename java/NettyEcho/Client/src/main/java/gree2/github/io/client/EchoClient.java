package gree2.github.io.client;

import io.netty.bootstrap.Bootstrap;
import io.netty.channel.ChannelFuture;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelPipeline;
import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.nio.NioSocketChannel;

import java.net.InetSocketAddress;
import java.nio.channels.SocketChannel;

/**
 * EchoClient
 *
 * User: houqiangliang
 * Date: 2016-06-14
 * Time: 15:58:01
 */
public class EchoClient {

    private final String host;
    private final int port;

    /**
     * echo client
     * @param host host
     * @param port port
     */
    public EchoClient(String host, int port){
        this.host = host;
        this.port = port;
    }

    /**
     * main
     * @param args args
     * @throws Exception
     */
    public static void main(String[] args) throws Exception{
        if (args.length != 2){
            System.err.println("usage: " + EchoClient.class.getSimpleName() + " <host>:<port>");
            return;
        }
        String host = args[0];
        int port = Integer.parseInt(args[1]);
        new EchoClient(host, port).start();
    }

    /**
     * start client
     * @throws Exception
     */
    public void start() throws  Exception{
        EventLoopGroup group = new NioEventLoopGroup();
        try {
            Bootstrap b = new Bootstrap();
            b.group(group)
                    .channel(NioSocketChannel.class)
                    .remoteAddress(new InetSocketAddress(host, port))
                    .handler(new ChannelInitializer<SocketChannel>() {
                        @Override
                        protected void initChannel(SocketChannel ch) throws Exception {
                            ch.pipeline().addLast(new EchoClientHandler());
                        }
                    });
            ChannelFuture f = b.connect().sync();
            f.channel().closeFuture().sync();
        } finally {
            group.shutdownGracefully().sync();
        }
    }
}
