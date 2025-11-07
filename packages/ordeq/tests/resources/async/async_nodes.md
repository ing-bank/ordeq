:::mermaid
graph TB
	subgraph legend["Legend"]
		direction TB
		subgraph Objects
			L0(["Node"]):::node
			L1[("IO")]:::io
		end
		subgraph IO Types
			L00[("StringBuffer")]:::io0
		end
	end

	write_buffer_2 --> IO0
	write_buffer_1 --> IO1

	subgraph pipeline["Pipeline"]
		direction TB
		write_buffer_2(["write_buffer_2"]):::node
		write_buffer_1(["write_buffer_1"]):::node
		IO0[("buffer_2")]:::io0
		IO1[("buffer_1")]:::io0
	end

	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5
:::


> This graph also applies to the `sync_nodes` example defined in the same resource.
