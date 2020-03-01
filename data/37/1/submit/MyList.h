#pragma once
#include <list>
#include <memory>

class MyList
{
private:
	std::shared_ptr< std::list<int> > pt;
	std::list<int>::iterator left, right;

	std::list<int>::iterator forward(int pos) const{
		auto now = left;
		while(pos--) now++;
		return now;
	}

public:
	MyList(): pt(new std::list<int>()){
		left = pt->begin();
		right = pt->end();
	}
	MyList(const MyList &b): pt(b.pt){
		left = b.left;
		right = b.right;
	}

	void append(int i){
		if(pt->size() == 0){
			pt->insert(right, i);
			left = pt->begin();
		}else{
			pt->insert(right, i);
		}
		

		//std::cout << "append" << i << std::endl;
		//std::cout << pt->size() << std::endl;
		//std::cout << *left << std::endl;
		//std::cout << *this << std::endl;
	}

	int& operator[](int pos) const{
		return *forward(pos);
	}

	MyList operator()(int l, int r) const{
		MyList res(*this);
		res.left = forward(l);
		res.right = forward(r);
		return res;
	}

	friend std::ostream& operator<<(std::ostream& out, const MyList & b){
		out << "[";
		if (b.left != b.right){
			auto now = b.left;
			out << *now;
			now ++;
			for(; now != b.right; now++){
				out << "," << *now;
			}
		}
		out << "]";
		return out;
	}

};