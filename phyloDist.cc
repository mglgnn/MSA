#include <iostream>
#include <string>
#include <list>
#include <vector>
using namespace std;

struct Node{
    Node() : pParent(NULL), pLeft(NULL), pRight(NULL), dist(0.0) {};
    Node(int nodeId) : id(nodeId), pParent(NULL), pLeft(NULL), pRight(NULL), dist(0.0) {};
    Node(int nodeId, string l) : label(l), id(nodeId), pParent(NULL), pLeft(NULL), pRight(NULL), dist(0.0) {};
    string label;
    int id;
    Node *pParent, *pLeft, *pRight;
    double dist;
};

void recDeleteNode(Node* pNode){
    if(pNode != NULL){
        if(pNode->pLeft)
            recDeleteNode(pNode->pLeft);
        if(pNode->pRight)
            recDeleteNode(pNode->pRight);
        
        #ifdef DEBUG
        cout << "deleting " << pNode->id << "," << pNode->label << endl;
        #endif
        
        delete pNode;
        pNode = NULL;
    }
}

Node* createTree(string s){
    int numNodes = 0;
    double dist;
    string sub;
    list<Node*> stack;
    list<Node*>::iterator itStack;
    Node *pNode = NULL, *pLeft = NULL, *pRight = NULL;

    // todo : use Tokenizer class
    int i=0, j;
    while(i<s.length()){
        if(s[i] == '('){
            // do nothing
            ++i;
            cout << "(" << endl;
        }
        else if(s[i] == ')'){
            ++i;
            // popA, popB, merge A and B an push back the result
            pNode = new Node(numNodes);
            ++numNodes;
            pNode->pLeft = stack.back();
            stack.pop_back();
            pNode->pRight = stack.back();

            pNode->pLeft->pParent = pNode->pRight->pParent = pNode;

            stack.pop_back();
            stack.push_back(pNode);



            cout << "pop1 " << pNode->pLeft->id << "," << pNode->pLeft->label << " pop2 " << pNode->pRight->id << "," << pNode->pRight->label << " pushed " << pNode->id << endl;

        }
        else if(s[i] == ':'){
            // read distance and set it as the distance for the node which is at the top of the stack
            ++i;
            j = i;

            while(j<s.length() && s[j]!=')' && s[j]!=',')
                ++j;
            if(j==s.length()){
                // free allocated memory and destroy the stack
                for(itStack=stack.begin();itStack!=stack.end();++itStack)
                    recDeleteNode(*itStack);
                stack.clear();

                cout << "Error 1 : string len exceeded..." << endl;
                return NULL;
            }

            sub = s.substr(i, j-i);
            dist = atof(sub.c_str());

            cout << "dist " << dist << " assigned to " << stack.back()->id << "," << stack.back()->label << endl;
            
            i = j;

            stack.back()->dist = dist;
            

        }
        else if(s[i] == ',' || s[i] == ';'){
            // do nothing
            ++i;
        }
        else {
            // read a new label
            j = i;
            while(j<s.length() && s[j]!=':')
                ++j;
            if(j==s.length()){
                // free allocated memory and destroy the stack
                for(itStack=stack.begin();itStack!=stack.end();++itStack)
                    recDeleteNode(*itStack);
                stack.clear();

                cout << "Error 2 : string len exceeded..." << endl;
                return NULL;
            }
            sub = s.substr(i, j-i);

            cout << "name " << sub << endl;

            i = j;            

            pNode = new Node(numNodes, sub);
            ++numNodes;

            stack.push_back(pNode);
        }
    }

    if(stack.size() != 1)
        cout << "Error in parsing..." << endl;
    else
        cout << "Correct parsing..." << endl;

    return stack.back();
}

Node* searchNode(Node* pNode, string label){
    if(pNode!=NULL){
        if(pNode->label == label)
            return pNode;
        Node* pTmp = searchNode(pNode->pLeft, label);
        if(pTmp != NULL)
            return pTmp;
        return searchNode(pNode->pRight, label);
    }
    return NULL;
}

double computeDist(Node* pTree, string labelA, string labelB){
    if(pTree == NULL){
        cout << "computeDist : NULL tree" << endl;
        return 0.0;
    }
    
    Node *pNodeA = NULL, *pNodeB = NULL;
    
    pNodeA = searchNode(pTree, labelA);
    if(pNodeA == NULL){
        cout << "computeDist : cannot find label " << labelA << endl;
        return 0.0;
    }

    #ifdef DEBUG
    cout << "found " << pNodeA->label << endl;
    #endif

    pNodeB = searchNode(pTree, labelB);
    if(pNodeB == NULL){
        cout << "computeDist : cannot find species " << labelB << endl;
        return 0.0;
    }   

    #ifdef DEBUG
    cout << "found " << pNodeB->label << endl;
    #endif

    list<Node*> pathToRootA, pathToRootB;
    Node *pScan = NULL;

    pScan = pNodeA;
    while(pScan != NULL){
        pathToRootA.push_back(pScan);
        pScan = pScan->pParent;
    }
    
    pScan = pNodeB;
    while(pScan != NULL){
        pathToRootB.push_back(pScan);
        pScan = pScan->pParent;
    }

    list<Node*>::reverse_iterator itrA = pathToRootA.rbegin(), itrB = pathToRootB.rbegin();
    while(itrA!=pathToRootA.rend() && itrB!=pathToRootB.rend() && *itrA == *itrB){
        ++itrA;
        ++itrB;
    }

    #ifdef DEBUG
    cout << "sizepat A to root " << pathToRootA.size() << endl;
    cout << "sizepat B to root " << pathToRootB.size() << endl;
    #endif

    double dist = 0.0;
    while(itrA!=pathToRootA.rend()){
        #ifdef DEBUG
        cout << "adding " << (*itrA)->dist << endl;
        #endif
        dist += (*itrA)->dist; 
        ++itrA;
    }
    while(itrB!=pathToRootB.rend()){
        #ifdef DEBUG
        cout << "adding " << (*itrB)->dist << endl;
        #endif
        dist += (*itrB)->dist; 
        ++itrB;
    }

    return dist;
}

void getLabelsRec(Node* pNode, vector<string>& labelArr){
    if(pNode!=NULL){
        if(pNode->pLeft==NULL && pNode->pRight==NULL)
            labelArr.push_back(pNode->label);
        else{
            getLabelsRec(pNode->pLeft, labelArr);
            getLabelsRec(pNode->pRight, labelArr);
        }
    }
}

// minimal tests follow
void test(Node* pTree){
    double dist;
    vector<string> labelArr;
    cout << "Minimal test started" << endl;    

    getLabelsRec(pTree, labelArr);

    cout << labelArr.size() << " labels at leaves found:";
    for(int i=0;i<labelArr.size();++i)
        cout << " " << labelArr[i];
    cout << endl; 

    for(int i=0;i<labelArr.size();++i){
        if(computeDist(pTree, labelArr[i], labelArr[i]) != 0)
            cout << "--- error in identity..." << endl;
    }
    
    for(int j, i=0;i<labelArr.size();++i){
        for(j=i+1;j<labelArr.size();++j){
            dist = computeDist(pTree,labelArr[i], labelArr[j]);
            if(abs(dist-computeDist(pTree, labelArr[j], labelArr[i])) > 1e-10)
                cout << "--- error in symmetry..." << endl;
        }
    }
    cout << "Minimal test ended" << endl;    
}

int main(int argc, char* argv[]){

    string s = "((((((((((((((((((hg38:0.00655,panTro4:0.00684):0.00422,gorGor3:0.008964):0.009693,ponAbe2:0.01894):0.003471,nomLeu3:0.02227):0.01204,(((rheMac3:0.004991,macFas5:0.004991):0.003,papAnu2:0.008042):0.01061,chlSab2:0.027000):0.025000):0.021830,(calJac3:0.03,saiBol1:0.010350):0.019650):0.072610,otoGar3:0.13992):0.013494,tupChi1:0.174937):0.002,(((speTri2:0.125468,(jacJac1:0.1,((micOch1:0.08,(criGri1:0.04,mesAur1:0.040000):0.040000):0.060000,(mm10:0.084509,rn6:0.091589):0.047773):0.060150):0.100000):0.022992,(hetGla2:0.1,(cavPor3:0.065629,(chiLan1:0.06,octDeg1:0.100000):0.060000):0.050000):0.060150):0.025746,(oryCun2:0.114227,ochPri3:0.201069):0.101463):0.015313):0.020593,(((susScr3:0.12,((vicPac2:0.047275,camFer1:0.04):0.04,((turTru2:0.034688,orcOrc1:0.039688):0.03,(panHod1:0.1,(bosTau8:0.1,(oviAri3:0.05,capHir1:0.050000):0.050000):0.010000):0.013592):0.025153):0.020335):0.020000,(((equCab2:0.059397,cerSim1:0.025):0.05,(felCat8:0.098612,(canFam3:0.052458,(musFur1:0.05,(ailMel1:0.02,(odoRosDiv1:0.02,lepWed1:0.020000):0.020000):0.030000):0.030000):0.020000):0.049845):0.006219,((pteAle1:0.05,pteVam1:0.063399):0.05,(eptFus1:0.02,(myoDav1:0.04,myoLuc2:0.042540):0.050000):0.060000):0.033706):0.004508):0.011671,(eriEur2:0.221785,(sorAra2:0.169562,conCri1:0.100000):0.100000):0.056393):0.021227):0.023664,(((((loxAfr3:0.002242,eleEdw1:0.05):0.04699,triMan1:0.1):0.049697,(chrAsi1:0.03,echTel2:0.235936):0.010000):0.030000,oryAfe1:0.03):0.02,dasNov3:0.169809):0.006717):0.234728,(monDom5:0.125686,(sarHar1:0.1,macEug2:0.072008):0.050000):0.215100):0.071664,ornAna1:0.456592):0.109504,(((((colLiv1:0.1,((falChe1:0.1,falPer1:0.1):0.03,(((ficAlb2:0.04,((zonAlb1:0.034457,geoFor1:0.041261):0.015,taeGut2:0.060000):0.010000):0.052066,pseHum1:0.06):0.025,(melUnd1:0.046985,(amaVit1:0.026,araMac1:0.026000):0.010000):0.040000):0.064703):0.060000):0.050000,(anaPla1:0.1,(galGal4:0.041254,melGal1:0.085718):0.031045):0.090000):0.220000,allMis1:0.25):0.045143,((cheMyd1:0.1,chrPic2:0.1):0.05,(pelSin1:0.1,apaSpi1:0.100000):0.050000):0.040000):0.010000,anoCar2:0.447000):0.122000):0.050000,xenTro7:0.977944):0.1,latCha1:0.977944):0.111354,(((((((tetNig2:0.124159,(fr3:0.103847,takFla1:0.100000):0.100000):0.097590,(oreNil2:0.1,(neoBri1:0.05,(hapBur1:0.05,(mayZeb1:0.05,punNye1:0.050000):0.050000):0.050000):0.100000):0.100000):0.097590,(oryLat2:0.38197,xipMac1:0.400000):0.100000):0.015000,gasAcu1:0.246413):0.045,gadMor1:0.25):0.22564,(danRer10:0.430752,astMex1:0.400000):0.300000):0.143632,lepOcu1:0.400000):0.326688):0.200000,petMar2:0.975747);";
    Node *pTree = createTree(s);

    test(pTree);

    
    
    double distSym, dist = computeDist(pTree, "hg38", "macFas5");
    cout << "dist(hg38,macFas5) = " << dist << endl;
    dist = computeDist(pTree, "hg38", "mm10");
    cout << "dist(hg38,mm10) = " << dist << endl;
    dist = computeDist(pTree, "hg38", "hetGla2");
    cout << "dist(hg38,hetGla2) = " << dist << endl;
    dist = computeDist(pTree, "mm10", "macFas5");
    cout << "dist(mm10, macFas5) = " << dist << endl;
    dist = computeDist(pTree, "mm10", "hetGla2");
    cout << "dist(mm10, hetGla2) = " << dist << endl;
    dist = computeDist(pTree, "macFas5", "hetGla2");
    cout << "dist(macFas5, hetGla2) = " << dist << endl;
    
   
    if(pTree)
        recDeleteNode(pTree);

    return 0;
}